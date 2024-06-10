from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_football_crazy, name='about'),
]