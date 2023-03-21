from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    date = models.DateField()
    description = models.TextField()


    def __str__(self):
        return self.title
