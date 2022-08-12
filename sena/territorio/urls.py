from django.urls import path
from . import views

app_name='territorio'

urlpatterns = [
    path("", views.index, name="index"),

    #Rutas aprendices
    path("aprendiz/", views.aprendiz, name="listar-aprendices"),
    path("crear-aprendiz/", views.aprendicesForm, name="crearAprendices"),
    path("guardar-aprendiz/", views.aprendicesGuardar, name="guardarAprendices"),

    #Rutas monitorias
    path("monitorias/", views.listarMonitoria, name="listar-monitoria"),
    path("crear-monitorias/", views.monitoriasForm, name="crearMonitoria"),
    path("guardar-monitorias/", views.monitoriasGuardar, name="monitoriasGuardar"),

    #Rutas actividades
    path("actividades/", views.listarActividades, name="listar-actividades"),
]