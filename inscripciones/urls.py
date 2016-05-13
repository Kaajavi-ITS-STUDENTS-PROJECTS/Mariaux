from django.conf.urls import patterns, include, url
from django.views.generic.edit import UpdateView

urlpatterns = patterns('',
                       url(r'^$',
                           'inscripciones.views.home',
                           name='home'),
                      url(r'^add_alumno$',
                         'inscripciones.views.add_alumno',
                         name='add'),)
