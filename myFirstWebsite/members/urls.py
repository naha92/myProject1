from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),  
    path('about/', views.about, name='aboutus'),
    path('team/', views.team, name='team'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),     
]