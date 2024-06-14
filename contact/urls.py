from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_football_crazy, name='contact'),
]
