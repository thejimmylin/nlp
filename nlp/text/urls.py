from django.urls import path
from .views import helloworld, index

urlpatterns = [
    path('helloworld/', helloworld, name='helloworld'),
    path('', index, name='index'),
]
