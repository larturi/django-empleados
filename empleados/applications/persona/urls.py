
from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
    path('listar-empleados/', views.ListEmpleados.as_view()),
    path('listar-empleados-departamento/<short_name>', views.ListEmpleadosByDepartamento.as_view()),
    path('listar-empleados-job/<job>', views.ListEmpleadosByPuesto.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('habilidades-empleado/<id>', views.ListHabilidadesEmpleado.as_view()),
    path('detalle-empleado/<pk>', views.EmpleadoDetailView.as_view()),
    path('add-empleado/', views.EmpleadoCreateView.as_view()),
    path('success/', views.SuccessView.as_view(), name='success'),
]
