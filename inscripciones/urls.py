from django.conf.urls import patterns, include, url
from django.views.generic.edit import UpdateView

urlpatterns = patterns('',
                       url(r'^$',
                          'inscripciones.views.abm_alumno',
                          name='alta_alumno'),
                       url(r'^edit/(?P<id_alumno>\d+)/$',
                          'inscripciones.views.abm_alumno',
                          name='edit_alumno'),
                       url(r'^foo',
                           'inscripciones.views.home',
                           name='home'),
                      url(r'^add_alumno$',
                         'inscripciones.views.add_alumno',
                         name='add'),)
