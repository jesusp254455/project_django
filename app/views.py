from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
# Create your views here.

def index(request):
    title = 'Django aprendiendo'
    return render( request, "index.html",{
        'titulo': title
    })

def hellow(request, name):
    print(name)
    return HttpResponse("hola %s" %name)

def about(request):
    return HttpResponse('About')

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html',{
        'pros':projects
    })

def task_view(request):
    tasks = Task.objects.all()  # Correct the typo 'objetcs' to 'objects'
    print(list(Task.objects.all()))
    return render(request,'task.html',{
        'task':tasks
    })

def task_2(request):
    return render(request,'create_task.html')

