from django.contrib import admin

# Register your models here.
from .models import Hero,About,Blog,Skill

admin.site.register(Hero)
admin.site.register(About)
admin.site.register(Blog)
admin.site.register(Skill)
