from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Estado
#ccbv.co.uk

class Estado_View(ListView):
	model = Estado
	fields='__all__'
	template_name = 'Estado/estado_list.html'

lista_estado = Estado_View.as_view()

class Estado_Create(CreateView):
	model = Estado
	template_name = 'Estado/estado_crear.html'
	fields='__all__'
	success_url = reverse_lazy('estado_crear')

crear_estado = Estado_Create.as_view()