from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Curso(models.Model):
    numero = models.IntegerField('Numero Curso')
    division = models.CharField('Division',max_length=1)

    def __str__(self):
        return str(self.numero) +" "+ self.division

class Alumno(models.Model):
    nombre = models.CharField('Nombre',max_length=16)
    apellido = models.CharField('Apellido',max_length=32)
    curso = models.ForeignKey(Curso,null=False)
    inscripto = models.BooleanField('Inscripto',default=False)

    def __str__(self):
        return self.nombre +" "+self.apellido
