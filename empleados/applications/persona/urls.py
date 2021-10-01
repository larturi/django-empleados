
from django.urls import path

def persona(self):
    print('persona')

urlpatterns = [
    path('persona/', persona),
]
