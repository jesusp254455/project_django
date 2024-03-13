from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('about/', views.about),
    path('hellow/<str:name>',views.hellow),
    path('projects/',views.projects),
    path('task/',views.task_view),
    path('task_create/', views.task_2)
]