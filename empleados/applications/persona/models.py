from django.db import models

from applications.departamento.models import Departamento

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = "Habilidades"
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return self.habilidad

class Empleado(models.Model):

    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Informatico'),
        ('3', 'Economista'),
        ('4', 'Otro'),
    )
    first_name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellido', max_length=100)
    job = models.CharField('Puesto', max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)

    def __str__(self):
        return str(self.id) + ' - ' + self.first_name + ' - ' + self.last_name
