from django.db import models

# Create your models here.

class Posts (models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    counter = models.PositiveIntegerField(default=0)


