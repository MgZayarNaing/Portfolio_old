from django.urls import path 
from myapp.views import  HeroSection,BlogSection,BlogDetail,ProjectSection

urlpatterns = [
     # path('home/', Resume),
     path('home/', HeroSection),

     path('blog/', BlogSection),
     path('project/', ProjectSection),
     path('blogdetail/<str:blog_id>/', BlogDetail),
     

]