from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse_lazy
from blog.models import Animal
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