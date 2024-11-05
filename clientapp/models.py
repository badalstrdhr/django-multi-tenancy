from django.db import models
from django_cassandra_engine.models import DjangoCassandraModel
# Create your models here.
from superadmin.models import *
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class Tenant(TenantMixin):
    t_email = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)

    auto_create_schema = True

class Domain(DomainMixin):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name="domains")
    domain_name = models.CharField(max_length=255)

    def __str__(self):
        return self.domain_name


