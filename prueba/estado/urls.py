from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^listar/$', views.lista_estado, name='estado_list'),
    url(r'^crear/$', views.crear_estado, name='estado_crear'),


]
