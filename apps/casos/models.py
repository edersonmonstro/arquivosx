from django.db import models

# Create your models here.
class CasosModel(models.Model):
    titulo = models.CharField(max_length = 400)
    tema = models.CharField(max_length = 50)

    def __str__(self):
        return self.titulo