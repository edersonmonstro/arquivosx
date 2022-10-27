from email.policy import default
from django.db import models
from django.contrib import admin

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField(null=True)
    def __str__(self):
        return self.name

class Suspect(models.Model):
    name = models.CharField(max_length = 100)
    acusation = models.CharField(max_length = 500)
    def __str__(self):
        return self.name

class Case(models.Model):
    title = models.CharField(max_length = 400)
    theme = models.CharField(max_length = 50)
    investigator = models.ForeignKey(Person, null=True, blank=True, on_delete=models.CASCADE)
    suspects = models.ManyToManyField(Suspect, blank=True)
    def __str__(self):
        return self.title
    def to_dict(self):
        d = { 'title' : self.title, 'theme' : self.theme }
        return d 
    def toJSON(self):
        return self.to_dict()

admin.site.register(Case)
admin.site.register(Suspect)
admin.site.register(Person)