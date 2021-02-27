from django.db import models

class RawData(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(verbose_name='дата запуска',auto_now_add=True)
    raw_data = models.TextField(verbose_name='сырые данные')

class Psychotherapists(models.Model):
    id = models.AutoField(primary_key=True)
    Имя = models.Charfield(max_length=50)
    Фотография = models.URLField()

# Create your models here.

