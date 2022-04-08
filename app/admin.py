from django.contrib import admin
from .models import Language


class LanguageAdmin(admin.ModelAdmin):
    list_display = ("uuid", "lang_code", "lang_name", "pass0_utt", "pass0_mcd", "pass1_utt", "pass1_mcd", "duration",
    "rfs_utt", "base", "rfs", "created_at", "updated_at"
    )


admin.site.register(Language, LanguageAdmin)