from django.db import models

from tinymce.models import HTMLField
class serviceBox(models.Model):
    service_icon = models.CharField(max_length=50)
    service_heading = models.CharField(max_length=50)
    service_content = HTMLField()


# Create your models here.
