from django.db import models


class Gra(models.Model):
    tytul = models.CharField(max_length=100)
    gatunek = models.CharField(max_length=50)
    ocena = models.IntegerField()
    cena = models.DecimalField(max_digits=6, decimal_places=2)
    dostepna = models.BooleanField(default=True)
    data_wydania = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.tytul} ({self.gatunek})"

