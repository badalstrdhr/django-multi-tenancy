from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password



from rest_framework import serializers, views, status
from rest_framework.response import Response
from django.db import transaction
from .models import Tenant, Domain
from django_tenants.utils import schema_context

class TenantRegistrationSerializer(serializers.ModelSerializer):
    raw_password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    tenant_name = serializers.CharField(write_only=True, required=True)
    domain_name = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()  
        fields = ['email', 'username', 'raw_password', 'tenant_name', 'domain_name']

    def create(self, validated_data):
        raw_password = validated_data.pop('raw_password')
        tenant_name = validated_data.pop('tenant_name')
        domain_name = validated_data.pop('domain_name')

        with transaction.atomic():
            user = get_user_model().objects.create(**validated_data)
            user.set_password(raw_password)
            user.save()

            tenant = Tenant.objects.create(name=tenant_name)

            domain = Domain.objects.create(tenant=tenant, domain_name=domain_name)

            tenant.create_schema()

            user.tenant = tenant
            user.save()

        return user






