# szotar_app/models.py

from django.db import models

class Szopar(models.Model):
    magyar = models.CharField(max_length=80)
    angol = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.magyar} - {self.angol}"
