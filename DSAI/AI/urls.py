from unicodedata import name
from django.urls import path
from AI import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('dataset/', views.getTestData, name='getTestData'),
    path('dataset/post/', views.setTestData, name='setTestData'),
    path('dataset/update/', views.updateTestData, name='updateTestData'),
    path('dataset/delete/', views.deleteTestData, name='deleteTestData')
]