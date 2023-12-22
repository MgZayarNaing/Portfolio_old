from django.urls import path 
from myapp.views import  HeroSection,BlogSection,SkillSection

urlpatterns = [
     # path('home/', Resume),
     path('home/', HeroSection),

     path('blog/', BlogSection),
     path('skill/', SkillSection),

]