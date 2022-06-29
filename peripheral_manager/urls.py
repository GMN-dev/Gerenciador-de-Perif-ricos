from django.urls import path
from peripheral_manager import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="index"),   
    
]   
