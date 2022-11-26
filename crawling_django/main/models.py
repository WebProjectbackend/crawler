from django.db import models

# Create your models here.
class article(models.Model):
    title = models.CharField()
    company = models.CharField()
    date = models.DateField()
    link = models.CharField()
