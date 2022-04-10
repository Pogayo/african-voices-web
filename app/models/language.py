from uuid import uuid4

from django.db import models

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
    countries = models.ManyToManyField(Country)

    def __str__(self) -> str:
        return self.lang_name

    @property
    def total_speakers(self) -> int:
        return self.lang_native_speakers + self.lang_non_native_speakers

    @property
    def all_countries(self) -> str:
        return ", ".join([country.name.capitalize() for country in self.countries.all()])

    @property
    def datasets(self):
        return self.dataset_set.all()


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
