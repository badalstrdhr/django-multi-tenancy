from django.contrib import admin
from .models import *
from django_tenants.admin import TenantAdminMixin


# Register your models here.

@admin.register(Tenant)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name',)
