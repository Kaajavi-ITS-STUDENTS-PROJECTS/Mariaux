from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
# Create your views here.
from django.contrib.auth.decorators import login_required
from models import  Curso , Alumno

@login_required(login_url="/404")
def home(request):
    context = RequestContext(request)
    context['cursos'] = Curso.objects.all()
    return render_to_response('index.html',context)

def add_alumno(request):
    context = RequestContext(request)
    if request.method == 'POST':
        nombre = request.POST['name']
        apellido = request.POST['surname']
        idcurso = request.POST['combo']
        curso = Curso.objects.get(pk=idcurso)
        alumno = Alumno()
        alumno.nombre=nombre
        alumno.apellido = apellido
        alumno.curso=curso
        alumno.save()
    return redirect("/")
