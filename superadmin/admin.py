from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'get_role', 'is_staff', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_staff', 'is_active', 'cu_role__rm_role')  

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password', 'raw_password', 'cu_role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'cu_role', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)

    def get_role(self, obj):
        return obj.cu_role.rm_role if obj.cu_role else 'No Role'
    get_role.short_description = 'Role'  

admin.site.register(CustomUser, CustomUserAdmin)





