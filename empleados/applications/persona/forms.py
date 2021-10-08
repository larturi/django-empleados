
from django import forms
from django.forms import widgets
from .models import Empleado

class EmpleadoUpdateForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'habilidades',
        )
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class':'form-control mb-2'}
            ),
            'last_name': forms.TextInput(
                attrs={'class':'form-control mb-2'}
            ),
            'job': forms.Select(
                attrs={'class':'form-control mb-2'}
            ),
            'departamento': forms.Select(
                attrs={'class':'form-control mb-2'}
            ),
            'habilidades': forms.SelectMultiple(
                attrs={'class':'form-control mb-2'}
            ),
        }
