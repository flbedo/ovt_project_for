from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('on/', views.set_on, name='set_on'),
    path('off/', views.set_off, name='set_off'),
]