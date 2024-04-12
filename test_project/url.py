from . import views
from django.urls import path


urlpatterns = [
    path("home", views.home , name="home"),
    path("test", views.test , name="test"),
    path("onama", views.onama , name="onama"),
    path("usluge", views.usluge , name="usluge"),
    path("galerija", views.galerija , name="galerija"),
    path("kontakt", views.kontakt , name="kontakt"),
    path("pitanje", views.pitanje , name="pitanje"),


  
]