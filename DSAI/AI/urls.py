from unicodedata import name
from django.urls import path
from AI import views

urlpatterns = [
    path('main/', views.main, name='main'),
]