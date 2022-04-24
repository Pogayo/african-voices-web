from django.db import models
from uuid import uuid4
from .language import Language
from .datasource  import DataSource

class Gender(models.TextChoices):
     MALE = 'Male'
     FEMALE = 'Female'
     NON_BINARY = 'Non binary'

class Dataset(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    data_id = models.CharField(max_length=100, unique=True)
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    source = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    speaker_gender = models.CharField(choices=Gender.choices, max_length=100, blank=True)
    pass0_utt = models.FloatField(max_length=100,  blank=True)
    pass0_mcd = models.FloatField(max_length=100, blank=True)
    pass1_utt = models.IntegerField(default=0)  # display
    pass1_mcd = models.FloatField(default=0)  # display
    duration = models.FloatField(default=0)
    data_location = models.CharField(max_length=256, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.data_id + " - " + str(self.lang)
