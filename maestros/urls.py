from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import create_maestro, create_user
from .views import MaestroListView, MaestroUpdateView, MaestroDetailView

urlpatterns = [

    path('registro/',create_user, name='nuevo usuario'),
    
    path('maestros/nuevo/',login_required(create_maestro),name='nuevo maestro'),

    path('maestros/update/<int:pk>',login_required(MaestroUpdateView.as_view()),name='update maestro'),

    path('maestros/lista/',login_required(MaestroListView.as_view()),name='lista maestros'),

    path('maestros/detalle/<int:pk>',login_required(MaestroDetailView.as_view()),name='detalle maestro'),

]

