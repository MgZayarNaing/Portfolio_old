from django.shortcuts import render
from myapp.models import Hero,About,Blog,Skill

# Create your views here.

def HeroSection(request):
    home = Hero.objects.all()
    about = About.objects.all()
    return render(request, 'index.html', {'home':home, 'about':about})


# BlogSection
def BlogSection(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', {'blog':blog})

# BlogSection
def SkillSection(request):
    skill = Skill.objects.all()
    return render(request, 'skill.html', {'skill':skill})