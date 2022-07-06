from django import views
from django.urls import path, include
#from Maestros import views
#from .views import *
from Maestros.views import inicio, fasesFormulario, fasesFormulario, peliculasFormulario, personajesFormulario, personajes_peliculaFormulario, busquedaPersonaje, resultadoPersonaje
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ # en el path inicio nos piden : path('', views.inicio, name = 'inicio'), corroborar
    path('inicio', views.inicio, name = 'inicio'),
    path('fasesFormulario/', fasesFormulario, name="fasesFormulario"),
    path('peliculasFormulario/', peliculasFormulario, name="peliculasFormulario"),
    path('personajesFormulario/', personajesFormulario, name="personajesFormulario"),
    path('personajes_peliculaFormulario/', personajes_peliculaFormulario, name="personajes_peliculaFormulario"),
    path('busquedaPersonaje/', busquedaPersonaje, name="busquedaPersonaje"),
    path('resultadoPersonaje/', resultadoPersonaje, name="resultadoPersonaje"),

    path('login/', views.login_request, name = 'Login'),
    path('registro', views.registro, name = 'Registro'),
    path('logout', LogoutView.as_view(template_name='Maestros/logout.html'), name = 'Logout'),

    path('editarPerfil', views.editarPerfil, name = 'editar_perfil'), 
    path('perfil/', views.perfil, name="perfil"),
    path('perfil_detail', views.perfil_detail, name = 'perfil_detail'),
]