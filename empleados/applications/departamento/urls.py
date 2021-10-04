
from django.urls import path
from . import views

urlpatterns = [
    path('new-departamento/', views.NewDepartamentoView.as_view(), name='new-departamento'),
]
