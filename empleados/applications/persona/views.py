from django.shortcuts import render
from datetime import date
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from django.views.generic import (
    ListView, 
    DetailView,
    CreateView
)

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

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        today = date.today()
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['edad'] = today.year - self.get_object().fecha_nacimiento.year - ((today.month, today.day) < (self.get_object().fecha_nacimiento.month, self.get_object().fecha_nacimiento.day))
        return context

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    fields = ('__all__')
    success_url = reverse_lazy('persona_app:success')

class SuccessView(TemplateView):
    template_name = "persona/success.html"
