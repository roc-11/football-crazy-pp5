from django.urls import path
from .import views

urlpatterns = [
    path('', views.add_subscriber, name='newsletters'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
    path('send-email/', views.send_newsletter, name='send_email'),
]
