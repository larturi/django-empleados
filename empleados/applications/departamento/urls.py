
from django.urls import path

def departamento(self):
    print('Hola')

urlpatterns = [
    path('departamento/', departamento),
]
