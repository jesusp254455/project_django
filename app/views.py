# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project
# Create your views here.

def index(request):
    return HttpResponse("pag principal")

def hellow(request, name):
    print(name)
    return HttpResponse("hola %s" %name)

def about(request):
    return HttpResponse('About')

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)