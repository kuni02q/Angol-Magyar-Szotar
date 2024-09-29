# szotar_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_szopar, name='add_szopar'),
    path('list/', views.list_szoparok, name='list_szoparok'),
    path('practice/', views.practice, name='practice'),
    path('quiz/', views.quiz, name='quiz'),
    path('results/', views.results, name='results'),
]
