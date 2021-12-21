from django.contrib import admin
from .models import Autor, Categorias, Post, Comentario


class CategoriasAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'estado', 'fecha_creacion',)


class ComentarioAdmin(admin.ModelAdmin):
    search_fields = ['titulo']
    list_display = ('titulo', 'contenido','post','autor_id', 'fecha_creacion',)


class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombres', 'apellido', 'email']
    list_display = ('nombres', 'apellido','password', 'email','estado','fecha_creacion','tipo')

class PostAdmin(admin.ModelAdmin):
    search_fields =['titulo', 'autor','categoria']
    list_display = ('titulo', 'autor', 'categoria', 'fecha_creacion', 'estado')

admin.site.register(Autor, AutorAdmin)
admin.site.register(Categorias, CategoriasAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comentario, ComentarioAdmin)