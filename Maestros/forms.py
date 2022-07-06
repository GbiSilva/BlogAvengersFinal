from django import forms
from Maestros.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FasesFormulario(forms.Form):
    nombre=forms.CharField(max_length=2)

class PeliculasFormulario(forms.Form):
    fases = Fases.objects.all()

    lista_fases = []
    for fase in fases:
        lista_fases = lista_fases + [('Fase ' + fase.nombre, fase.nombre)]
    
    nombre=forms.CharField(max_length=40)
    sinopsis=forms.CharField(widget=forms.Textarea)
    anio=forms.IntegerField()
    duracion=forms.IntegerField()
    nombre_fase=forms.ChoiceField(widget=forms.RadioSelect, choices=lista_fases)
    
class PersonajesFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    superpoder=forms.CharField(max_length=30)
    actor_apellido=forms.CharField(max_length=30)
    actor_nombre=forms.CharField(max_length=30)
    
class Personajes_PeliculaFormulario(forms.Form):
    peliculas = Peliculas.objects.all()
    lista_peliculas = []
    for pelicula in peliculas:
        lista_peliculas = lista_peliculas + [(pelicula.nombre, pelicula.nombre)]

    personajes = Personajes.objects.all()
    lista_personajes = []
    for personaje in personajes:
        lista_personajes = lista_personajes + [(personaje.nombre, personaje.nombre)]

    nombre_personaje=forms.ChoiceField(widget=forms.RadioSelect, choices=lista_personajes)
    nombre_pelicula=forms.ChoiceField(widget=forms.RadioSelect, choices=lista_peliculas)



class UserRegistrationForm(UserCreationForm):
  username = forms.CharField()
  email = forms.EmailField(required=True)
  password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
  password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

  last_name = forms.CharField()
  first_name = forms.CharField()
  class Meta: 
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    help_texts={k:"" for k in fields} ## {{ form.as_p }}
class UserEditForm(UserCreationForm):
  email = forms.EmailField(required=True)
  password1 = forms.CharField(label="Modificar Contraseña", widget=forms.PasswordInput, required=False)
  password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)
  first_name = forms.CharField(label="Modificar Nombre")
  last_name = forms.CharField(label="Modificar Apellido") 

  class Meta: ## Campos que muestra, no olvidar 
    model = User
    fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
    help_texts={k:"" for k in fields} # {{ form.as_p }}

class Perfil(forms.Form):   
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email= forms.EmailField()    
    
    class Meta: # Campos que muestra, no olvidar 
      model = User
      fields = ['first_name', 'last_name', 'email']       