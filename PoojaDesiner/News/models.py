from django.db import models

from tinymce.models import HTMLField

class NewsBox(models.Model):
    title = models.CharField(max_length=50)
    content = HTMLField()
# Create your models here.
