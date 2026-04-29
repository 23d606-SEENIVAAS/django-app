from django.urls import path
from myapp import views

urlpatterns = [
    path('health', views.health_check),
]