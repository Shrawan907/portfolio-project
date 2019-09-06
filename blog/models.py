from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
