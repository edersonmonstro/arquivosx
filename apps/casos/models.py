from django.db import models

# Create your models here.
class SuspectModel(models.Model):
    name = models.CharField(max_length = 100)
    acusation = models.CharField(max_length = 500)
    def __str__(self):
        return self.name

class CasosModel(models.Model):
    titulo = models.CharField(max_length = 400)
    tema = models.CharField(max_length = 50)
    suspeitos = models.ManyToManyField(SuspectModel)
    def __str__(self):
        return self.titulo