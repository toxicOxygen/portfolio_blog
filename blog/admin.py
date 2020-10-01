from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','publish','status']
    list_filter = ['publish','updated']
    list_editable = ['status']
    search_fields = ['title','body']
    prepopulated_fields = {'slug':('title',)}