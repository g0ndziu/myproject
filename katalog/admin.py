from django.contrib import admin
from .models import Gra

class GraAdmin(admin.ModelAdmin):
    list_display = ('tytul', 'gatunek', 'ocena', 'cena', 'dostepna', 'wydawca', 'opis')
    list_filter = ('gatunek', 'dostepna', 'wydawca')
    search_fields = ('tytul', 'wydawca')

admin.site.register(Gra, GraAdmin)