from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.postres import postres
from main.forms import contactform


# Create your views here.
def index(req):
    context= {'postres':postres }
    return render(req,'index.html',context)

def about(req):
    return render(req, 'about.html')

def welcome(req):
    if req.method == 'GET':
        form = contactform()
        context = {'form': form}
        return render(req, 'welcome.html', context)
    else:
        form = contactform(req.POST)
    if form.is_valid():
        return redirect('/contactus')
    context = {'form': form}
    return render(req, 'welcome.html', context)

def exito(req):
  return HttpResponse('Eeeexito!!!!')

def contactus(req):
    return render(req, 'contactus.html')
