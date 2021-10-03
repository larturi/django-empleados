from django.shortcuts import render
from django.views.generic import ListView
from .models import Empleado

class ListEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 3
    model = Empleado


class ListEmpleadosByDepartamento(ListView):
    template_name = 'persona/list-by-departamento.html'

    def get_queryset(self):
        departamento = self.kwargs['short_name']
        lista = Empleado.objects.filter(departamento__short_name=departamento.upper())
        return lista

class ListEmpleadosByPuesto(ListView):
    template_name = 'persona/list-by-puesto.html'

    def get_queryset(self):
        job = self.kwargs['job']
        lista = Empleado.objects.filter(job=job)
        return lista

class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_keyword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(first_name=palabra_clave)
        return lista

class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        id = self.kwargs['id']
        empleado = Empleado.objects.get(id=id)
        return empleado.habilidades.all()