from django.shortcuts import render
from datetime import date
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.db.models import Q

from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .forms import EmpleadoUpdateForm, EmpleadoCreateForm

from .models import Empleado

class InicioView(TemplateView):
    template_name = "inicio.html"

class ListEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(Q(first_name__icontains=palabra_clave) | Q(last_name__icontains=palabra_clave))

        return lista

class ListEmpleadosByDepartamento(ListView):
    template_name = 'persona/list-by-departamento.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'

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
    form_class = EmpleadoCreateForm
    success_url = reverse_lazy('persona_app:empleados')

    def form_valid(self, form):
        empleado = form.save()
        # Aqui puedo agregar logica extra
        return super(EmpleadoCreateView, self).form_valid(form)

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    form_class = EmpleadoUpdateForm
    success_url = reverse_lazy('persona_app:empleados')

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/persona-delete.html"
    success_url = reverse_lazy('persona_app:empleados')
class SuccessView(TemplateView):
    template_name = "persona/success.html"


