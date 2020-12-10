from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


from .forms import MaestroCreationForm
from .models import Maestro

# Create your views here.

def create_user(request):
    if request.method == 'POST':

        user_form = UserCreationForm(request.POST)

        if user_form.is_valid():
            user_form.save()
            user = user_form.cleaned_data
            username = user['username']
            password = user['password1']

            new_user = authenticate(username=username,password=password)
            login(request,new_user)

            return redirect('nuevo maestro')
    
    else:
        user_form = UserCreationForm()

    context = {
        'user_form': user_form,
    }
    return render(request, 'nuevo_usuario.html', context)


@login_required
def create_maestro(request):
    if request.method == 'POST':
        form = MaestroCreationForm(request.POST, request.FILES,instance=request.user.maestro)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = MaestroCreationForm()
        
    context = {
        'form': form,
    }
    return render(request, 'nuevo_maestro.html', context)


class MaestroUpdateView(UpdateView):

    model = Maestro
    fields = [
        'nombres',
        'apellidos',
        'telefono',
        'email',
        'nacimiento',
        'foto',
    ]
    template_name = 'update_maestro.html'
    success_url = reverse_lazy('home')


    def get(self, request, *args, **kwargs):
        userpk = self.request.user.maestro.pk
        requested_pk = self.kwargs['pk']
        form = self.get_form()

        if userpk == requested_pk:
            return super().get(request,*args,**kwargs)

        else:
            raise PermissionDenied()