from django.urls import path 
from myapp.views import  HeroSection

urlpatterns = [
     # path('home/', Resume),
     path('home/', HeroSection),


]