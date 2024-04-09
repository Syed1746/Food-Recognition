from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Define a URL pattern for the home view
    path('service2', views.service2, name='service2'),  # Define a URL pattern for the service2 view
]