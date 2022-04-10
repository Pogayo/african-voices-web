from django.db import models
from uuid import uuid4
from .language import Language



class Dataset(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    data_id = models.CharField(max_length=100, unique=True)
    lang_id = models.ForeignKey(Language, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    pass0_utt = models.CharField(max_length=100)
    pass0_mcd = models.CharField(max_length=100)
    pass1_utt = models.CharField(max_length=100) #display
    pass1_mcd = models.CharField(max_length=100) #display
    duration = models.CharField(max_length=100)
    data_location = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.data_id + " - " + self.lang_id.lang_id