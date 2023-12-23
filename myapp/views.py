from django.shortcuts import render
from myapp.models import Hero,About,Blog,Skill,Contact,Project

# Create your views here.

def HeroSection(request):
    home = Hero.objects.all()
    about = About.objects.all()
    skill = Skill.objects.all()
    contact = Contact.objects.all()
    project = Project.objects.all().order_by('-created_at')[:3]
    blog = Blog.objects.all().order_by('-created_at')[:3]
    return render(request, 'index.html', { 'home':home, 'about':about, 'skill':skill, 'blog':blog, 'contact':contact, 'project':project })


# BlogSection
def BlogSection(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', {'blog':blog})

# ProjectSection
def ProjectSection(request):
    project = Project.objects.all()
    return render(request, 'project.html', {'project':project})