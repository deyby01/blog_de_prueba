from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion')
    search_fields = ('titulo', 'contenido')
    list_filter = ('fecha_publicacion',)
