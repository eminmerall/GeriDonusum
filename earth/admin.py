from django.contrib import admin
from .models import kullanici, firma, randevu


class adminKullanici(admin.ModelAdmin):
    list_display = ["kId", "kAdi", "kSoyadi"]
    list_display_links = ["kId", "kAdi", "kSoyadi"]
    list_filter = ["kAdi", "kSoyadi"]
    search_fields = ["kAdi", "kSoyadi"]

    class Meta:
        model = kullanici

class adminFirma(admin.ModelAdmin):
    list_display = ["fId", "fAdi"]
    list_display_links = ["fId", "fAdi"]
    list_filter = ["fAdi"]
    search_fields = ["fAdi"]

    class Meta:
        model = firma

class adminRandevu(admin.ModelAdmin):
    list_display = ["rId", "aTuru", "rTarih", "rSaat"]
    list_display_links = ["rId", "aTuru", "rTarih", "rSaat"]
    list_filter = ["rId", "aTuru", "rTarih", "rSaat"]
    search_fields = ["rId", "aTuru", "rTarih", "rSaat"]

    class Meta:
        model = randevu


# Register your models here.
admin.site.register(kullanici, adminKullanici)
admin.site.register(firma, adminFirma)
admin.site.register(randevu, adminRandevu)



