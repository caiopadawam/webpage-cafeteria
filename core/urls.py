from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo', views.catalogo_cafe, name='catalogo')
]