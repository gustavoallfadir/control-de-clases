from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import home_view, aprobar_clase, rechazar_clase
from .views import ClaseCreateView, ClaseListView, ClasePorAprobarListView

urlpatterns = [
    path('',home_view, name='home'),
    path('guardar_clase/', login_required(ClaseCreateView.as_view()),name='nueva clase'),
    path('clases/lista/', login_required(ClaseListView.as_view()),name='lista clases'),        
    path('clases/por_aprobar/', login_required(ClasePorAprobarListView.as_view()),name='clases por aprobar'),

    path('clases/aprobar/<pk>',aprobar_clase,name='aprobar clase'),
    path('clases/rechazar/<pk>',rechazar_clase,name='rechazar clase'),
]

