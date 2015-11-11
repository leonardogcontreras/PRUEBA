from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^listar/$', views.lista_mascota, name='mascota_list'),
    url(r'^crear/$', views.crear_mascota, name='mascota_crear'),


]
