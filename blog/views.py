from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.admin import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from blog.models import Animal, Adopcion
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from blog.forms import AdopcionForm, NewUserForm


def about(request):
    return render(request, 'blog/about.html')

    
def index(request):
     animal = Animal.objects.order_by('-fecha_publicacion').all()
     return render(request, 'blog/index.html', {"animal": animal})

class AnimalList(ListView):
    adopcion = Adopcion.objects.all()
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
    model= Adopcion
    form_class = AdopcionForm
    template_name = 'blog/adopcion_form.html'
    success_url = reverse_lazy('adopcion_listar')
    
    def actualizar(self, request, pk): 
      animal = get_object_or_404(Animal, pk=pk)
      form = self.form_class(request.POST ,instance=animal)
      if form.is_valid():
          animal.estado =False
          animal.save()
          form.save()
      return render(request, self.template_name)
'''
    def actualizar_estado(self, request, pk):
        a = get_object_or_404(Animal, pk=pk)
        a.estado=False
        a.save()

    def actualizar(self, request, pk):
        animal = get_object_or_404(Animal, pk=pk)
        animal.estado=False
        animal.save()       
        return render(request, self.template_name) 
'''
     

                

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
    form_class = NewUserForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy("blog-login")
    

class ProfileUpdate(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy("blog-login")