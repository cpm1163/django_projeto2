from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('HOME')
    # return HTTP response

def contato(request):
    return HttpResponse('CONTATO')
    # return HTTP response
    # return HTTP response

def sobre(request):
    return HttpResponse('SOBRE')
    # return HTTP response