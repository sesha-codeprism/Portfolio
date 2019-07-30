from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to ='images/')
    sumry = models.CharField(max_length =200)
