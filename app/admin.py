from django.contrib import admin
from .models import *

class LanguageAdmin(admin.ModelAdmin):
    list_display = ("uuid", "lang_code", "lang_name", "pass0_utt", "pass0_mcd", "pass1_utt", "pass1_mcd", "duration",
    "rfs_utt", "base", "rfs", "created_at", "updated_at"
    )

class CountryAdmin(admin.ModelAdmin):
    list_display = ("uuid", "code", "name")

class LanguageCountryAdmin(admin.ModelAdmin):
    list_display = ("uuid", "language", "country")


admin.site.register(Language, LanguageAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(LanguageCountry, LanguageCountryAdmin)
