from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Perfil_Mascota
#ccbv.co.uk

class Mascota_View(ListView):
	model = Perfil_Mascota
	fields='__all__'
	template_name = 'Mascotas/mascota_list.html'

lista_mascota = Mascota_View.as_view()

class Mascota_Create(CreateView):
	model = Perfil_Mascota
	template_name = 'Mascotas/mascota_crear.html'
	fields='__all__'
	success_url = reverse_lazy('mascota_crear')

crear_mascota = Mascota_Create.as_view()