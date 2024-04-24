from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('docente/', views.docente, name='docente'),
    path('alumno/', views.alumno, name='alumno'),
]