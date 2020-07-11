from django.shortcuts import render

from django.views.generic import (
    TemplateView, 
    ListView,
    CreateView
)
    

from .models import Prueba

from .forms import PruebaForm

# Create your views here.
class PruebaView(TemplateView):
    template_name='home/prueba.html'

class ResumeFoundationView(TemplateView):
    template_name='home/resume_foundation.html'

class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name='ListaNumeros'
    queryset = ['0','10','20','30']


class ListaPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name='lista'



class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    #fields = ['titulo','subtitulo','cantidad']
    form_class = PruebaForm
    success_url = '/'


