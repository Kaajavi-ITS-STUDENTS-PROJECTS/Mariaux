from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
# Create your views here.
from django.contrib.auth.decorators import login_required
from models import  Curso , Alumno
from .forms import AlumnoForm

@login_required(login_url="/404")
def home(request):
    context = RequestContext(request)
    context['cursos'] = Curso.objects.all()
    return render_to_response('index.html',context)

def abm_alumno(request, id_alumno=None):
    '''
    Si pasas un id, editas, si no, creas uno nuevo
    '''
    context = RequestContext(request)
    if (id_alumno!=None):
        alumno = Alumno.objects.get(pk=id_alumno)
    else:
        alumno = Alumno()

    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.save()
            rev = reverse('home:edit_alumno', args=[alumno.id])
            return redirect(rev)
    else:
        form=AlumnoForm(instance=alumno)
    context['form']=form
    return render(request, 'abm_alumno.html',context)



def visor(request):
    form = []
    numero = [1,2,3,4,5,7]
    division = ['A','B','C']
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.inscripto = True
            print alumno
            alumno.save()
            return redirect('/')
    else:
        for n in numero:
            for d in division:
                cur = Curso.objects.all().filter(numero=n,division=d)
                alumnos = Alumno.objects.all().filter(curso = cur)
                for alumno in alumnos:
                    form.append(AlumnoForm(instance=alumno))
        return render(request, 'visor.html', {'forms': form})



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
