from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models

class RoleModel(models.Model):
    rm_role = models.CharField(max_length=128, unique=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.rm_role

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, raw_password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password) 
        user.raw_password = raw_password  
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, raw_password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, raw_password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)  
    password = models.CharField(max_length=128)  
    raw_password = models.CharField(max_length=128, blank=True, null=True) 
    cu_role = models.OneToOneField(RoleModel, on_delete=models.CASCADE, related_name="superadmin")
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='deleted_users')
    updated_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='updated_users')

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',  
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions', 
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'cu_role']  

    objects = CustomUserManager()

    def __str__(self):
        return self.email
