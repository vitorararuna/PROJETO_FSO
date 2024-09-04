from datetime import datetime
from typing import Any
from django.db import models
from django.conf import settings
from django.utils import timezone

class Turma(models.Model):
    name = models.CharField(max_length=100)
    matutino = models.BooleanField(default=False)
    vespertino = models.BooleanField(default=False)
    trilha = models.CharField(max_length=100)
    max_size = models.IntegerField(default=0)
    vagas = models.IntegerField(default=0)

    def getMatutino(self):
        return self.matutino

    def getVespertino(self):
        return self.vespertino

    def __str__(self):
        return self.name

class Person(models.Model):
    CPF = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.CPF
    

    
class Student(Person):
    turma = models.ForeignKey(Turma, null=True, on_delete=models.SET_NULL, blank=True)
    matriculado = models.BooleanField(default=False)
    entry_time = models.DateTimeField(default=timezone.now)

    

    def timeLimit(self):
        return timezone.now() + datetime.timedelta(seconds=30)
    
    def setTimeLimit(self):
        self.entry_time = timezone.now()
        self.save()
class Admin(Person):
    pass

# Create your models here.