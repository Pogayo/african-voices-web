from django.db import models
from uuid import uuid4
from .language import *
from .dataset import Dataset


class Synthesizer(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    synth_id = models.CharField(max_length=100, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    rfs_utt = models.CharField(max_length=100)
    base = models.CharField(max_length=100)
    rfs = models.CharField(max_length=100)
    data_location = models.CharField(max_length=256)
    flite_location = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.synth_id + " - " + self.language.language_name + " - " + self.dataset.dataset_name


class SynthesizerSamples(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    synth = models.ForeignKey(Synthesizer, on_delete=models.CASCADE)
    lang_sample = models.ForeignKey(LanguageSample, on_delete=models.CASCADE)
    sample_location = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lang_sample + " --> synthesizer : " + self.synth.synth_id
