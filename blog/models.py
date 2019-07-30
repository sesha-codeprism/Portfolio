from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    pubdate = models.DateTimeField()
    body = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
