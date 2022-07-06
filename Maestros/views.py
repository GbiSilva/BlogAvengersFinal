from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from Maestros.forms import *


# Login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin #para los crud
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def inicio(self):
    plantilla=loader.get_template('Maestros/inicio.html')
    documento=plantilla.render()
    return HttpResponse(documento)
# Cambiar los request de los return por Maestros
def fasesFormulario(request):
    if request.method == 'POST':
        mi_formulario = FasesFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nombre = informacion['nombre']
            grabar = Fases(nombre=nombre)
            grabar.save()
            return render(request, 'MarvelApp/inicio.html')
    else:
        mi_formulario = FasesFormulario()
    return render(request, 'MarvelApp/fasesFormulario.html', {'mi_formulario':mi_formulario})

def peliculasFormulario(request):
    if request.method == "POST":
        mi_formulario = PeliculasFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nombre = informacion['nombre']
            sinopsis = informacion['sinopsis']
            anio = informacion['anio']
            duracion = informacion['duracion']
            nombre_fase = informacion['nombre_fase']
            grabar = Peliculas(nombre=nombre, sinopsis=sinopsis, anio=anio, duracion=duracion, nombre_fase=nombre_fase)
            grabar.save()
            return render(request, 'MarvelApp/inicio.html')
    else:
        mi_formulario = PeliculasFormulario()
        return render(request, 'MarvelApp/peliculasFormulario.html', {'mi_formulario':mi_formulario})

def personajesFormulario(request):
    if request.method == "POST":
        mi_formulario = PersonajesFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nombre = informacion['nombre']
            superpoder = informacion['superpoder']
            actor_apellido = informacion['actor_apellido']
            actor_nombre = informacion['actor_nombre']
            grabar = Personajes(nombre=nombre,superpoder=superpoder, actor_apellido=actor_apellido, actor_nombre=actor_nombre)
            grabar.save()
            return render(request, 'MarvelApp/inicio.html')
    else:
        mi_formulario = PersonajesFormulario()
        return render(request, 'MarvelApp/personajesFormulario.html', {'mi_formulario':mi_formulario})

def personajes_peliculaFormulario(request):
    if request.method == "POST":
        mi_formulario = Personajes_PeliculaFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nombre_personaje = User.objects.get(nombre_personaje=request.POST['nombre_personaje'])
            nombre_pelicula = informacion['nombre_pelicula']
            grabar = Personajes_Pelicula(nombre_personaje=nombre_personaje, nombre_pelicula=nombre_pelicula)
            grabar.save()
            return render(request, 'MarvelApp/inicio.html')
    else:
        mi_formulario = Personajes_PeliculaFormulario()
        return render(request, 'MarvelApp/personajes_peliculaFormulario.html', {'mi_formulario':mi_formulario})

def busquedaPersonaje(request):
    return render(request, 'MarvelApp/busquedaPersonaje.html')

def resultadoPersonaje(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        personajes = Personajes.objects.filter(nombre=nombre)
        respuesta = render(request, 'MarvelApp/resultadobusquedaPersonaje.html', {'personajes':personajes,'nombre':nombre} )
        return HttpResponse(respuesta)
    else:
        respuesta = "No se ha ingresado el personaje a buscar"
        return HttpResponse(respuesta)

#login y registro
def login_request(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      usuario = form.cleaned_data.get("username")
      clave = form.cleaned_data.get("password")
      user = authenticate(username=usuario, password=clave) 
      if user is not None:
        login(request,user) 
        return redirect('inicio')#tenemos que corregir
      else:
        messages.error(request, "Los datos son incorrectos")
    else:
      messages.error(request, "Los datos son incorrectos")

  form = AuthenticationForm()
  return render(request, 'Maestros/login.html', {'form': form})


def registro(request):
  data ={
      'form' : UserRegistrationForm()
  }
  if request.method == 'POST': #
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      
      form.save()
      usuario = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
      login(request, usuario)
      messages.success(request, f'{usuario} Te has registrado correctamente')
      return redirect(to='inicio')
    data['form'] = form
  return render(request,'Maestros/registro.html', data)


@login_required()
def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario.first_name = data["first_name"]
            usuario.last_name=data["last_name"]
            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.save()
            return redirect("inicio")
            messages.success(request, "El perfil fue editado correctamente")
        else:
           
         
          form = UserEditForm(initial={"email":usuario.email})
        return render(request, 'Maestros/editar_perfil.html', {"title": "Editar usuario", "message": "Editar usuario", "form": form, "errors": ["Datos inválidos"]}) 
    
    else:
        form = UserEditForm(initial={"email":usuario.email})
        return render(request, 'Maestros/editar_perfil.html', {"title": "Editar usuario", "message": "Editar usuario", "form": form})



def perfil(request):
    return render(request, 'Maestros/perfil.html')    

def perfil_detail(request):
    return render(request, "Maestros/perfil_detail.html")
 

#CRUD tenemos que definir si vamos a usar con usuario, o sea nosotros, los listview, detailview, etc.
#Ejemplo de clase 
'''class EstudiantesList(LoginRequiredMixin, ListView):
  model = Estudiante
  template_name = 'AppCoder/estudiante_list.html'

class EstudianteDetalle(DetailView):
  model = Estudiante
  template_name = 'AppCoder/estudiante_detalle.html'

class EstudianteCreacion(CreateView):
  model = Estudiante
  success_url = reverse_lazy('estudiante_listar') # Redirecciono a la vista de estudiantes luego de crear un estudiante
  fields = ['nombre', 'apellido', 'email']

class EstudianteEdicion(UpdateView):
  model = Estudiante
  success_url = reverse_lazy('estudiante_listar')
  fields = ['nombre', 'apellido', 'email']

class EstudianteEliminacion(DeleteView):
  model = Estudiante
  success_url = reverse_lazy('estudiante_listar')'''