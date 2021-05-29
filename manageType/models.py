from django.db import models
from colorfield.fields import ColorField

# Create your models here.
class Type(models.Model):
    sortCd = models.IntegerField(verbose_name='順番', unique=True)
    name = models.CharField(verbose_name='名前', max_length=10)
    color = ColorField(verbose_name='表示色', default='#FF0000')