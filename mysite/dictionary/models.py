from django.db import models

# Create your models here.
class Dict(models.Model):
    originalW = models.CharField(max_length=20, unique=True)
    translationW = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.originalW