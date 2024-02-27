from django.db import models


class serviceBox(models.Model):
    service_icon = models.CharField(max_length=50)
    service_heading = models.CharField(max_length=50)
    service_content = models.TextField()


# Create your models here.
