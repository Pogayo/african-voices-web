from django.db import models
from uuid import uuid4
from .country import Country


class Language(models.Model):
    uuid = models.CharField(primary_key=True, unique=True, default=uuid4, max_length=100)
    lang_id = models.CharField(max_length=100)
    lang_code = models.CharField(max_length=100)
    lang_name = models.CharField(max_length=100)
    pass0_utt = models.CharField(max_length=100)
    pass0_mcd = models.CharField(max_length=100)
    pass1_utt = models.CharField(max_length=100)
    pass1_mcd = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    rfs_utt = models.CharField(max_length=100)
    base = models.CharField(max_length=100)
    rfs = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.lang_name

class LanguageCountry(models.Model):
    uuid = models.CharField(primary_key=True, unique=True, default=uuid4, max_length=100)
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
