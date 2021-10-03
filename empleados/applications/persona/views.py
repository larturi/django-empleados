from django.shortcuts import render
from django.views.generic import ListView
from .models import Empleado

class ListEmpleados(ListView):
    template_name = 'persona/list_all.html'
    model = Empleado


class ListEmpleadosByDepartamento(ListView):
    template_name = 'persona/list-by-departamento.html'
    queryset = Empleado.objects.filter(departamento__name="Marketing")