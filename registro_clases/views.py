from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required, permission_required

from .models import Clase
from maestros.models import Maestro
from .forms import ClaseCreateForm

# Create your views here.

def home_view(request):
    ultimas_clases = Clase.objects.all()[:10]
    ultimos_maestros = Maestro.objects.all()[:5]
    context = {
        'clases':ultimas_clases,
        'maestros':ultimos_maestros,
    }
    return render(request,'index.html',context=context)


class ClaseCreateView(CreateView):
    model = Clase
    form_class = ClaseCreateForm
    success_url = reverse_lazy('home')
    template_name = ('crear_clase.html')

    def form_valid(self, form):
        clase = form.save(commit=False)
        clase.maestro = Maestro.objects.get(usuario=self.request.user)
        clase.save()
        return super().form_valid(form)


class ClaseListView(ListView):
    model = Clase
    context_object_name = 'clases'
    template_name = 'lista_clases.html'
    paginate_by = 30


class ClasePorAprobarListView(ListView):
    model = Clase
    context_object_name = 'clases'
    queryset = Clase.objects.filter(aprobada=False)
    template_name = 'clases_por_aprobar.html'
    paginate_by = 30


@login_required
def aprobar_clase(request,pk):
    "Vista de aprobación de clase"

    clase = Clase.objects.get(pk=pk)
    if clase:
        clase.aprobada = True
        clase.save()

        return HttpResponseRedirect(reverse_lazy('clases por aprobar'))
    
    else:
        return HttpResponseRedirect(reverse_lazy('404'))


@login_required
def rechazar_clase(request,pk):
    "Vista de rechazo de clase"
      
    clase = Clase.objects.get(pk=pk)
    
    if clase:
        clase.rechazada = True
        clase.save()
        return HttpResponseRedirect(reverse_lazy('clases por aprobar'))

    else:
        return HttpResponseRedirect(reverse_lazy('404'))


#VISTAS DE ERROR CUSTOM (SOLO EN PRODUCCION)
def error_403(request,exception):
        context = {}
        return render(request,'error_403.html', context)

def error_404(request,exception):
        context = {}
        return render(request,'error_404.html', context)