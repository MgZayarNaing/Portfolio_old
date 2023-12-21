from django.shortcuts import render
from myapp.models import Hero

# Create your views here.
# def home(request):
#     return render(request, 'index.html')

# def Resume(request):
#     home = Cv.objects.all()
#     return render(request, 'index.html', {'home':home})

def HeroSection(request):
    home = Hero.objects.all()
    return render(request, 'index.html', {'home':home})