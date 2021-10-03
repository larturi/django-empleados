
from django.urls import path
from . import views


urlpatterns = [
    path('listar-empleados/', views.ListEmpleados.as_view()),
    path('listar-empleados-departamento/<short_name>', views.ListEmpleadosByDepartamento.as_view()),
    path('listar-empleados-job/<job>', views.ListEmpleadosByPuesto.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('habilidades-empleado/<id>', views.ListHabilidadesEmpleado.as_view()),
]
