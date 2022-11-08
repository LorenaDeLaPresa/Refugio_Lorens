from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse_lazy
from blog.models import Animal, Adopcion
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from blog.models import Configuracion



def index(request):
     animal = Animal.objects.order_by('-fecha_publicacion').all()
     return render(request, 'blog/index.html', {"animal": animal})

class AnimalList(ListView):
    model = Animal
    template_name = 'blog/animal_list.html'
    paginate_by = 5    
    ordering = ['id']
    


class AnimalCreate(CreateView):
    model = Animal
    fields =['nombre', 'clase_animal', 'sexo', 'edad_aproximada','descripcion', 'foto'] 
    template_name = 'blog/animal_form.html'
    success_url = reverse_lazy('animal_listar')

class AnimalUpdate(UpdateView):
    model = Animal
    fields =['nombre', 'clase_animal', 'sexo', 'edad_aproximada', 'descripcion', 'foto'] 
    template_name = 'blog/animal_form.html'
    success_url = reverse_lazy('animal_listar')

class AnimalDelete(DeleteView):
    model = Animal
    template_name = 'blog/animal_confirm_delete.html'
    success_url = reverse_lazy('animal_listar')

class AnimalDetail(DetailView):
    model=Animal

class BuscarAnimalPorNombre(ListView):
    def get_queryset(self):
        animal_nombre = self.request.GET.get('animal-nombre')
        return Animal.objects.filter(nombre__icontains=animal_nombre)

class AdopcionList(ListView):
    model = Adopcion
    template_name = 'blog/adopcion_list.html'
    paginate_by = 5    
    ordering = ['id']

class AdopcionCreate(CreateView):
    model = Adopcion 
    fields =['usuario', 'animal', 'razones']  
    initial = {"usuario":Adopcion.usuario}
    
    template_name = 'blog/adopcion_form.html'
    success_url = reverse_lazy('adopcion_listar')
    
    def post(request, id_animal, template= 'blog/adopcion_form.html'):
        animal= get_object_or_404(Animal, pk = id_animal)
        animal.estado = False
        animal.save()

class AdopcionUpdate(UpdateView):
    model = Adopcion
    fields =['usuario', 'animal', 'razones']  
    template_name = 'blog/adopcion_form.html'
    success_url = reverse_lazy('adopcion_listar')

class AdopcionDelete(DeleteView):
    model = Adopcion
    template_name = 'blog/adopcion_confirm_delete.html'
    Animal.estado =True
    success_url = reverse_lazy('adopcion_listar')


class AdopcionDetail(DetailView):
    model=Adopcion

class BlogLogin(LoginView):
    template_name = 'blog/blog_login.html'
    next_page = reverse_lazy("animal_listar")

class BlogLogout(LogoutView):
    template_name = 'blog/blog_logout.html'
    
class BlogSignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("blog-login")
    template_name = "registration/signup.html"

    

class ProfileUpdate(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy("blog-login")