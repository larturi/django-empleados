from django.db import models
from django.db.models.fields import CharField

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre Corto', max_length=20, unique=True)
    habilitado = models.BooleanField('Habilitado', default=True)

    class Meta:
        verbose_name = "Departamanto"
        verbose_name_plural = "Departamentos"
        ordering = ['name']
        unique_together = ('name', 'short_name')

    def __str__(self):
        return str(self.id) + ' - ' + self.name