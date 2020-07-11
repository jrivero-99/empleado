from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
#models
from .models import Empleado
#forms
from .forms import EmpleadoForm
# Create your views here.

class InicioView(TemplateView):
    """ Vista que carga la página de inicio  """
    template_name="inicio.html"


class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name='empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista


class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name='empleados'
    model = Empleado


class ListByAreaEmpleado(ListView):
    """ Lista empleados de un area """
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departameto__shor_name = area
        )
        return lista


class ListEmpleadosByKword(ListView):
    """ Lista empleados por palabra clave """
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        return lista


class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=1)
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context
    

class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    # fields = ['first_name', 
    #          'last_name', 
    #          'job', 
    #          'departameto',
    #          'habilidades'
    #]  esta es una forma pero tendríamos que ecribir todos los campos que necesitamos
    #fields = ('__all__')   jala todos los campos del modelo
    #quitamos campos y usamos formularios
    #fields = [
    #    'first_name',
    #    'last_name',
    #    'job',
    #    'departameto',
    #    'avatar',
    #    'habilidades',
    #    'hoja_vida'
    #]
    form_class = EmpleadoForm

    #success_url = '.' # se recarga la misma página
    #success_url = '/success' # se recarga la misma página
    success_url = reverse_lazy('persona_app:empleados_admin') # importado de django.urls 

    def form_valid(self, form):
        #logica del proceso
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name +' ' +empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = ('__all__')
    success_url = reverse_lazy('persona_app:empleados_admin')
    #success_url = reverse_lazy('persona_app:correcto')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        #print('****** METODO POST *******')
        #print('==========================')
        #print(request.POST)
        #print('==========================')
        #print(request.POST['last_name']) # se accesa a un diccionario de django
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        #logica del proceso
        #print('****** FORM VALID ********')
        #print('==========================')
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name +' ' +empleado.last_name
        empleado.save()
        return super(EmpleadoUpdateView, self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    template_name = "persona/delete.html"
    model = Empleado
    #success_url = reverse_lazy('persona_app:correcto')
    success_url = reverse_lazy('persona_app:empleados_admin')
    
