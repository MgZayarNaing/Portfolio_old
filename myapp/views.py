from django.shortcuts import render,redirect
from myapp.models import Hero,About,Blog,Skill,Contact,Project,ContactMessage

# Create your views here.

def HeroSection(request):
    if request.method == "GET":

        home = Hero.objects.all()
        about = About.objects.all()
        skill = Skill.objects.all()
        contact = Contact.objects.all()
        project = Project.objects.all().order_by('-created_at')[:3]
        blog = Blog.objects.all().order_by('-created_at')[:3]
        contactmessage = ContactMessage.objects.all()
        return render(request, 'index.html', { 'home':home, 'about':about, 'skill':skill, 'blog':blog, 'contact':contact, 'project':project, 'contactmessage':contactmessage })

    if request.method == "POST":
        contactmessage = ContactMessage.objects.create(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            message = request.POST.get('message'),
        )

        return redirect('/app/home/')

# BlogSection
def BlogSection(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', {'blog':blog})

def BlogDetail(request,blog_id):
    blogdetail = Blog.objects.get(uuid=blog_id)
    return render(request, 'blogdetail.html', {'blogdetail':blogdetail})

# ProjectSection
def ProjectSection(request):
    project = Project.objects.all()
    return render(request, 'project.html', {'project':project})

