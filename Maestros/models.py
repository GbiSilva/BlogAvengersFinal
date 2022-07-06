from django.db import models
from django.contrib.auth.models import User

class Fases(models.Model):
    nombre=models.CharField(max_length=2, help_text="Ingrese el nro de fase en numeros romanos")
    def __str__(self) -> str:
        return self.nombre

class Peliculas(models.Model):
    nombre=models.CharField(max_length=40, help_text="Ingrese el nombre de la película")
    sinopsis=models.TextField(help_text="Ingrese el resumen de la película")
    anio=models.IntegerField(help_text="Ingrese el año de estreno  de la película")
    duracion=models.IntegerField(help_text="Ingrese la duración en minutos de la película")
    orden_cronologico=models.IntegerField(help_text="Ingrese el nro de orden de visualización")
    fase=models.ForeignKey(Fases, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.nombre+" "+str(self.anio) 
    
class Personajes(models.Model):
    nombre=models.CharField(max_length=30, help_text="Ingrese el nombre del personaje")
    superpoder=models.CharField(max_length=30, help_text="Ingrese el superpoder del personaje")
    actor_apellido=models.CharField(max_length=30, help_text="Ingrese el apellido del actor")
    actor_nombre=models.CharField(max_length=30, help_text="Ingrese el nombre del actor")
    def __str__(self) -> str:
        return self.nombre+" "+self.superpoder
    
class Personajes_Pelicula(models.Model):
    personaje=models.ForeignKey(Personajes, on_delete=models.CASCADE)
    pelicula=models.ForeignKey(Peliculas, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.personaje + "-" + self.personaje
        
# ejemplo que se me ocurrio como usuarios 
'''class Usuaios(models.Model):
    nombre = models.CharField(max_length=40)  
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    imagen = models.URLField(max_length = 255, blank = False, null= False)
    
    class Meta:
        verbose_name_plural = "Autores"
        verbose_name = "Autor"

    def __str__(self): 
        return f"{self.nombre}  {self.apellido} - {self.email}"'''

# Acá vendria el avatar