# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hellow(request):
    return HttpResponse("hola mundo")

def about(request):
    return HttpResponse('About')
