from uuid import uuid4

from django.db import models

from .country import Country


class LangFamily(models.TextChoices):
    NIGER_CONGO = "Niger–Congo"
    AUSTRONESIAN = "Austronesian"
    TRANS_NEW_GUINEA = "Trans–New Guinea"
    SINO_TIBETAN = "Sino-Tibetan"
    INDO_EUROPEAN = "Indo-European"
    AUSTRALIAN = "Australian"
    AFRO_ASIATIC = "Afro-Asiatic"
    NILO_SAHARAN = "Nilo-Saharan"
    OTO_MANGUEAN = "Oto-Manguean"
    AUSTROASIATIC = "Austroasiatic"
    TAI_KADAI = "Tai–Kadai"
    DRAVIDIAN = "Dravidian"
    TUPIAN = "Tupian"


class Language(models.Model):
    uuid = models.CharField(primary_key=True, unique=True, default=uuid4, max_length=100)
    lang_code_639_2 = models.CharField(max_length=100)
    lang_code_639_1 = models.CharField(max_length=100)
    lang_name = models.CharField(max_length=100)
    lang_family = models.CharField(choices=LangFamily.choices, max_length=100, blank=True)
    lang_native_speakers = models.IntegerField(default=0)
    lang_non_native_speakers = models.IntegerField(default=0)
    lang_wikipedia_url = models.CharField(max_length=200, blank=True)
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

    @property
    def synthesizers(self):
        return self.synthesizer_set.all()

    @property
    def samples(self):
        return self.language_sample_set.all()


class LanguageSample(models.Model):
    uuid = models.CharField(primary_key=True, unique=True, default=uuid4, max_length=100)
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING, related_name="language_sample_set")
    sample_id = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    pronunciation = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "lang: " + str(self.language) + ": text: " + self.text

    @property
    def synthesizer_samples(self):
        return self.synthesizer_samples_set.all()


class AddLanguage(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    wikipedia_url = models.CharField(max_length=200, blank=True)
    comment = models.TextField(max_length=100000, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self)-> str:
        return self.name+" ("+self.email+")"
