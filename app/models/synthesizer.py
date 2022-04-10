from django.db import models

from .dataset import Dataset
from .language import *


class Synthesizer(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    synth_id = models.CharField(max_length=100, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    rfs_utt = models.IntegerField(default=0)
    mcd_base = models.FloatField(default=0)
    mcd_rfs = models.FloatField(default=0)
    data_location = models.CharField(max_length=256)
    flite_location = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.synth_id + " - " + str(self.dataset)


class SynthesizerSample(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    synth = models.ForeignKey(Synthesizer, on_delete=models.CASCADE)
    lang_sample = models.ForeignKey(LanguageSample, on_delete=models.CASCADE)
    sample_location = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.lang_sample) + " --> synthesizer : " + self.synth.synth_id
