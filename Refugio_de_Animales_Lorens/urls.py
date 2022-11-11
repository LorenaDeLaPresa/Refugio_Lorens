"""Refugio_de_Animales_Lorens URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from blog.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name="index-blog"),
    path('list/', AnimalList.as_view(), name="animal_listar"),
    path('create/', AnimalCreate.as_view(), name="animal_alta"),
    path('detail/<int:pk>/', AnimalDetail.as_view(), name="detail-animal"),
    path('update/<int:pk>/', AnimalUpdate.as_view(), name="animal_modificar"),
    path('delete/<int:pk>', AnimalDelete.as_view(), name="animal_borrar"),
    path('search-by-name/', BuscarAnimalPorNombre.as_view(), name="buscar_por_nombre"),
    path('login/', BlogLogin.as_view(), name="blog-login"),
    path('logout/', BlogLogout.as_view(), name="blog-logout"),
    path('signup/', BlogSignUp.as_view(), name="blog-signup"),
    path('user-profile/<int:pk>', ProfileUpdate.as_view(), name="profile-update"),
    path('list_adopcion/', AdopcionList.as_view(), name="adopcion_listar"),
    path('create_adopcion/<int:pk>/', AdopcionCreate.as_view(), name="adopcion_alta"),
    path('detail_adopcion/<int:pk>/', AdopcionDetail.as_view(), name="adopcion_detail"),
    path('update_adopcion/<int:pk>/', AdopcionUpdate.as_view(), name="adopcion_modificar"),
    path('delete_adopcion/<int:pk>', AdopcionDelete.as_view(), name="adopcion_borrar"),
    path('about', about, name='about'),
 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)