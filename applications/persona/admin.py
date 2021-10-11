from django.contrib import admin
from datetime import date

from .models import Empleado, Habilidades
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'fecha_nacimiento',
        'edad',
    )

    def edad(self, obj):
        today = date.today()
        return today.year - obj.fecha_nacimiento.year - ((today.month, today.day) < (obj.fecha_nacimiento.month, obj.fecha_nacimiento.day))

    search_fields = ('first_name', 'last_name')
    list_filter = ('departamento', 'job', 'habilidades')
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)
