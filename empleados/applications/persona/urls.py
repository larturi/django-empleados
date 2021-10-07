
from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
    path(
        '', 
        views.InicioView.as_view(), 
        name='inicio'
    ),
    path(
        'listar-empleados/', 
        views.ListEmpleados.as_view(), 
        name='empleados'
    ),
    path(
        'detalle-empleado/<pk>', 
        views.EmpleadoDetailView.as_view(),
        name='empleado_detail'
    ),
    path(
        'listar-empleados-departamento/<short_name>', 
        views.ListEmpleadosByDepartamento.as_view(),
        name='listar_empleados_departamento'
    ),
    path(
        'update-empleado/<pk>', 
        views.EmpleadoUpdateView.as_view(), 
        name='update_empleado'
    ),
    path(
        'delete-empleado/<pk>', 
        views.EmpleadoDeleteView.as_view(), 
        name='delete_empleado'
    ),


    # PARA ELIMINAR
    path('listar-empleados-job/<job>', views.ListEmpleadosByPuesto.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('habilidades-empleado/<id>', views.ListHabilidadesEmpleado.as_view()),
    path('add-empleado/', views.EmpleadoCreateView.as_view()),
    path('success/', views.SuccessView.as_view(), name='success'),
]
