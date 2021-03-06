from django.contrib import admin
from .models import *
from .models.datasource  import DataSource


class SynthesizeRequest(object):
    pass


@admin.register(Language, Country,  LanguageSample, Dataset, Synthesizer, DataSource, SynthesizerSample,SynthesizeRequestModel, AddLanguage)
class UniversalAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
