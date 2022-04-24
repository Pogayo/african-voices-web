from django.db import models
from uuid import uuid4

class DataSource(models.Model):
    uuid = models.CharField(primary_key=True, unique=True, default=uuid4, max_length=100)
    source_id = models.CharField(max_length=100, unique=True, default=uuid4)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    licence = models.CharField(max_length=100, blank=True)
    num_languages = models.IntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name