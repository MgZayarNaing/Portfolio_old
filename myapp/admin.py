from django.contrib import admin

# Register your models here.
from .models import Hero,About,Blog,Skill,Contact,Project,ContactMessage

admin.site.register(Hero)
admin.site.register(About)
admin.site.register(Blog)
admin.site.register(Skill)
admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(ContactMessage)
