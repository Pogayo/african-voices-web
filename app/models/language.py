from django.db import models
from uuid import uuid4
from .country import Country


class Language(models.Model):
    uuid = models.CharField(primary_key=True, unique=True, default=uuid4, max_length=100)
    lang_code_639_2 = models.CharField(max_length=100)
    lang_code_639_1 = models.CharField(max_length=100)
    lang_name = models.CharField(max_length=100)
    lang_native_speakers = models.IntegerField(default=0)
    lang_non_native_speakers = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.lang_name


class LanguageCountry(models.Model):
    uuid = models.CharField(primary_key=True, unique=True, default=uuid4, max_length=100)
    language = models.ManyToManyField(Language)
    country = models.ManyToManyField(Country)


class LanguageSample(models.Model):
    uuid = models.CharField(primary_key=True, unique=True, default=uuid4, max_length=100)
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING)
    sample_id = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    pronunciation = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "lang: " + str(self.language) + ": text: " + self.text
