from django.urls import path 
from myapp.views import  HeroSection,BlogSection,BlogDetail

urlpatterns = [
     # path('home/', Resume),
     path('home/', HeroSection),

     path('blog/', BlogSection),
     path('blogdetail/<str:blog_id>/', BlogDetail),
     

]