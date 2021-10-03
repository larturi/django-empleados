
from django.urls import path
from . import views


urlpatterns = [
    path('listar-empleados/', views.ListEmpleados.as_view()),
    path('listar-empleados-departamento/', views.ListEmpleadosByDepartamento.as_view()),
]
