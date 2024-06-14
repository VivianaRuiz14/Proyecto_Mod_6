from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.postres import postres
from main.forms import contactform
from main.models import contacto, Flan
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView

class loginviewpropia(SuccessMessageMixin ,LoginView):
      success_message = 'Has ingresado correctamente'


# Create your views here.

def about(req):
    return render(req, 'about.html')

def contact(req):
    if req.method == 'GET':
        form = contactform()
        context = {'form': form}
        return render(req, 'contact.html', context)
    else:
        form = contactform(req.POST)
        if form.is_valid():
            contacto.objects.create(
                **form.cleaned_data
            )
            return redirect('/contactus')
        context = {'form': form}
        return render(req, 'contact.html', context)
# def welcome(req):
#     # deme mostrar sólo los flanes privados de la base de datos
#     context= {'postres':postres }
#     return render(req,'welcome.html',context)

def exito(req):
  return HttpResponse('Eeeexito!!!!')

def contactus(req):
    return render(req, 'contactus.html')


@login_required
def welcome(req):
    # debe mostros solo los flanes privados de la base de datos

    flanes_privados = Flan.objects.filter(is_private=True)
    context ={
        'flanes':flanes_privados
    }
    return render(req,'welcome.html', context)

def index(req):
    # deme mostrar todos los flanes de la base de datos
    
    flanes_publicos = Flan.objects.filter(is_private=False)
    context ={
        'flanes':flanes_publicos
    }
    return render(req, 'index.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, "¡Has salido exitosamente!")
    return redirect('/')

def ayuda(req):
    return render(req, 'help.html')