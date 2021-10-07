from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView

from .forms import NewDepartamentoForm
from applications.persona.models import Empleado
from .models import Departamento

class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    paginate_by = 4
    ordering = 'name'
    context_object_name = 'departamentos'

class NewDepartamentoView(FormView):
    template_name = 'departamento/new.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):

        departamento = form.cleaned_data['departamento']
        shortname = form.cleaned_data['shortname']

        depto = Departamento(
            name = departamento,
            short_name = shortname
        )

        depto.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '1',
            departamento = depto,
            fecha_nacimiento = '2000-01-01'
        )

       
        return super(NewDepartamentoView, self).form_valid(form)