
from django import forms
from .models import Empleado

class EmpleadoUpdateForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'fecha_nacimiento',
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
            'fecha_nacimiento': forms.DateInput(
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

class EmpleadoCreateForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'fecha_nacimiento',
            'job',
            'departamento',
            'habilidades',
            'avatar',
        )
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class':'form-control mb-2'}
            ),
            'last_name': forms.TextInput(
                attrs={'class':'form-control mb-2'}
            ),
            'fecha_nacimiento': forms.DateInput(
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
            'avatar': forms.FileInput(
                attrs={'class':'form-control mb-2'}
            ),
        }

