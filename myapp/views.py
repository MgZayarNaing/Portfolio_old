from django.shortcuts import render
from myapp.models import Hero,About,Blog

# Create your views here.

def HeroSection(request):
    home = Hero.objects.all()
    return render(request, 'index.html', {'home':home})

# AboutSection
def AboutSection(request):
    about = About.objects.all()
    return render(request, 'index.html', {'about':about})

# BlogSection
def BlogSection(request):
    blog = Blog.objects.all()
    return render(request, 'index.html', {'blog':blog})