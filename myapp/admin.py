from django.contrib import admin

# Register your models here.
from .models import Hero,About,Blog

admin.site.register(Hero)
admin.site.register(About)
admin.site.register(Blog)
