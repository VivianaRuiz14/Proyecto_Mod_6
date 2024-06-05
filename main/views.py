from django.http import HttpResponse
from django.shortcuts import render
from main.postres import postres

# Create your views here.
def index(req):
    context= {'postres':postres }
    return render(req,'index.html',context)

def about(req):
    return render(req, 'about.html')

def welcome(req):
    return render(req, 'welcome.html')
