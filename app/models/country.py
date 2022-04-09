from django.db import models
from uuid import uuid4


class Country(models.Model):
    uuid = models.CharField(
    primary_key=True,
    unique=True,
    default=uuid4,
    max_length=100)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)