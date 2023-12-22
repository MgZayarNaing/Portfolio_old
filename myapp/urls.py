from django.urls import path 
from myapp.views import  HeroSection,AboutSection,BlogSection

urlpatterns = [
     # path('home/', Resume),
     path('home/', HeroSection),
     path('about/', AboutSection),
     path('blog/', BlogSection),


]