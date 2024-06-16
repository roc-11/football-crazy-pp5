from django.urls import path
from .import views

urlpatterns = [
    path('', views.add_subscriber, name='newsletters'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
]