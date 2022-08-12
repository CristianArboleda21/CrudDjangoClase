from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Aprendiz, Monitoria, Actividades 
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, "territorio/index.html")

#CRUD aprendices

def aprendiz(request):
    q = Aprendiz.objects.all()
    context = {'datos':q}
    return render(request, "territorio/aprendiz/listarAprendiz.html", context)

def aprendicesForm(request):
    return render(request, "territorio/aprendiz/formAprendiz.html")

def aprendicesGuardar(request):
    try:
        q = Aprendiz(
            cedula = request.POST['cedula'],
            nombre = request.POST['nombre'],
            apellido = request.POST['apellido'],
            fecha_nacimiento = request.POST['fecha_nacimiento']
        )
        q.save()
        #return HttpResponse("Aprendiz guardado <br/> <a href='../aprendiz/'>Listar aprendiz</a>")
        return HttpResponseRedirect(reverse('territorio:aprendices'))
    except Exception as e:
        return HttpResponse("Error: " + str(e))


#CRUD monitorias

def listarMonitoria(request):
    m = Monitoria.objects.all()
    context = {'datosM':m}
    return render(request, "territorio/monitoria/listarMonitoria.html", context)

def monitoriasForm(request):
    m = Aprendiz.objects.all()
    context = {'datos':m}
    return render(request, "territorio/monitoria/formMonitoria.html", context)

def monitoriasGuardar(request):
    try:
        a = Aprendiz.objects.get(pk = request.POST['aprendiz'])

        q = Monitoria(
            cat = request.POST['cat'],
            aprendiz = a,
            fecha_Inicio = request.POST['fecha_Inicio'],
            fecha_Final = request.POST['fecha_Final']
        )
        q.save()

        """
            cat = request.POST['cat'],
            aprendiz = request.POST['aprendiz']
            fecha_Inicio = request.POST['fecha_Inicio'],
            fecha_Final = request.POST['fecha_Final']

            a = Aprendiz.objects.get(id='aprendiz')
            crear = Monitoria.objects.create(cat=cat, aprendiz=a, fecha_Inicio,fecha_Final)
        
        """
        return HttpResponseRedirect(reverse('territorio:listar-monitoria'))
    except Exception as e:
        return HttpResponse("Error" + str(e))


#CRUD actividades

def listarActividades(request):
    ac = Actividades.objects.all()
    context = {'datosAc':ac}
    return render(request, "territorio/actividades/listarActividades.html", context)

