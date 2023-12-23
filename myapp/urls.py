from django.urls import path 
from myapp.views import  HeroSection,BlogSection

urlpatterns = [
     # path('home/', Resume),
     path('home/', HeroSection),

     path('blog/', BlogSection),

]