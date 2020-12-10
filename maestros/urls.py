from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import create_maestro, create_user, MaestroUpdateView

urlpatterns = [

    path('registro/',create_user, name='nuevo usuario'),
    
    path('crear_maestro/',login_required(create_maestro),name='nuevo maestro'),

    path('update_maestro/<int:pk>',login_required(MaestroUpdateView.as_view()),name='update maestro'),
]

