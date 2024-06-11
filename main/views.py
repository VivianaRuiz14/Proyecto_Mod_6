from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.postres import postres
from main.forms import contactform
from main.models import contacto 


# Create your views here.
def index(req):
    # deme mostrar todos los flanes de la base de datos
    context= {'postres':postres }
    return render(req,'index.html',context)

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
def welcome(req):
    # deme mostrar sólo los flanes privados de la base de datos
    context= {'postres':postres }
    return render(req,'welcome.html',context)

def exito(req):
  return HttpResponse('Eeeexito!!!!')

def contactus(req):
    return render(req, 'contactus.html')
