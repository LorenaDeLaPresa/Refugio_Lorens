from django.db import models



class Configuracion(models.Model):
    nombre_blog = models.CharField(max_length=15)
    titulo_blog = models.CharField(max_length=35)
    subtitulo_blog=models.CharField(max_length= 45)
    creado_por= models.CharField(max_length=45)


class Animal(models.Model):
    nombre = models.CharField(max_length=50)
    clase_animal= models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    descripcion = models.TextField(max_length=3000)
    fecha_publicacion = models.DateTimeField()
    foto = models.ImageField(upload_to="posts", null=True, blank=True)
    

'''class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    domicilio = models.TextField()
    
    def __str__(self):
        return '{}'.format(self.nombre+" "+self.apellidos)
    

'''