from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('about/', views.about),
    path('hellow/<str:name>',views.hellow),
    path('projetcs/',views.projects)
]