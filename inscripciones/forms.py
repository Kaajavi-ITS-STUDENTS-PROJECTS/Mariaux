from django import forms
from models import Alumno, Curso

class AddAlumnoForm(forms.ModelForm):
    curso = forms.ModelChoiceField(queryset=Curso.objects.all())
    class Meta:
        model = Alumno
        fields = ('nombre','apellido')
