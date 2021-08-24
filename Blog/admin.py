from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Post)
class Admin_Post(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']