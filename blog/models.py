from django.db import models
from django.contrib.auth.admin import User



class Animal(models.Model):
    nombre = models.CharField(max_length=50)
    clase_animal= models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    descripcion = models.TextField(max_length=3000)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to="posts", null=True, blank=True)
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        if self.estado :
            return '{}'.format(self.nombre+" "+self.clase_animal)
        return '{}'.format(self.nombre+" "+self.clase_animal)


class Adopcion(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, null=True, blank=True,on_delete=models.CASCADE)
    razones = models.TextField()
    fecha_adopcion = models.DateTimeField(auto_now_add=True)


