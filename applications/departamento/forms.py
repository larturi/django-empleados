from django import forms

class NewDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    shortname = forms.CharField(max_length=20)

    def __init__(self, *args, **kwargs):
        super(NewDepartamentoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
