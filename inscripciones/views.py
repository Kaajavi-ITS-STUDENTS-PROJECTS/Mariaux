from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
# Create your views here.
from django.contrib.auth.decorators import login_required
from models import  Curso , Alumno
from forms import AddAlumnoForm

@login_required(login_url="/404")
def home(request):
    context = RequestContext(request)
    context['cursos'] = Curso.objects.all()
    context['alumnos'] = Alumno.objects.all()
    return render_to_response('index.html',context)

def add_alumno(request):
    context = RequestContext(request)
    add_form = AddAlumnoForm()
    if request.method == 'POST':
        add_form = AddAlumnoForm(request.POST)
        if  (add_form.is_valid()):
            nombre = add_form.cleaned_data['nombre']
            apellido = add_form.cleaned_data['apellido']
            idcurso = add_form.cleaned_data['curso']
            curso = Curso.objects.get(pk=idcurso)
            alumno = Alumno()
            alumno.nombre=nombre
            alumno.apellido = apellido
            alumno.curso=curso
            alumno.save()
            return redirect("/")
    return render(request, 'index.html', {'form': add_form})
