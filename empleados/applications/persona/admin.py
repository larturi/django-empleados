from django.contrib import admin

from .models import Empleado, Habilidades
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
    )

    search_fields = ('first_name', 'last_name')

    list_filter = ('departamento', 'job')

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)
