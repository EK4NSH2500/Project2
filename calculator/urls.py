from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('air-calculator/result-air-calcultator/', views.calculateair),
    path('air-calculator/', views.index1),
    path('water-calculator/result-water-calculator/', views.calculatewater),
    path('water-calculator/', views.index2),
    path('solid-calculator/result-solid-calculator/', views.calculatesolid),
    path('solid-calculator/', views.index3)

]