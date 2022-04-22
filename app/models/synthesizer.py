from django.db import models

from .dataset import Dataset
from .language import *


class Synthesizer(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    synth_id = models.CharField(max_length=100, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    rfs_utt = models.IntegerField(default=0)
    rfs_hrs = models.FloatField(default=0.0)
    mcd_base = models.FloatField(default=0)
    mcd_rfs = models.FloatField(default=0)
    is_main = models.BooleanField(default=False)
    data_location = models.CharField(max_length=256)
    flite_location = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.synth_id + " - " + str(self.dataset)




class SynthesizerSample(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    synth = models.ForeignKey(Synthesizer, on_delete=models.CASCADE)
    lang_sample = models.ForeignKey(LanguageSample, on_delete=models.CASCADE, related_name='synthesizer_samples_set')
    sample_location = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.lang_sample) + " --> synthesizer : " + self.synth.synth_id
AUDIO_FORMAT = [('mp3', 'mp3'),
                ('wav', 'wav')]


class SynthesizeRequestModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    text = models.TextField(max_length=100000)
    audio_format = models.CharField(max_length=3, choices=AUDIO_FORMAT, default='mp3')
    synth_id = models.CharField(max_length=1000, default='', choices=[])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.synth_id