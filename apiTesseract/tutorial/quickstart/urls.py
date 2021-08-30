from django.urls import path

from . import views

urlpatterns = [
    path('', views.Arquivo, name='index'),
]
