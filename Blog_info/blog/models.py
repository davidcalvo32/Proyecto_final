from django import forms
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class Categorias(models.Model):
    cat_id = models.AutoField(primary_key= True)
    nombre = models.CharField('Nombre de la categoría', max_length=100, null=False, blank=False)
    descripcion = models.CharField('Descripción de la categoría', max_length=200, null=False, blank=False, default="Descripción de la categoría")
    estado = models.BooleanField('Categoría Activa/Categoría Inactiva', default= True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.nombre
    
class Autor(models.Model):
    au_id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres del Autor', max_length=150, null= False, blank=False)
    apellido = models.CharField('Apellido del Autor', max_length=150, null= False, blank=False)
    password = forms.PasswordInput()
    web = models.URLField('Red social/website', null = True, blank = True)
    email = models.EmailField('Correo electronico', null = False, blank=False)
    estado = models.BooleanField('Autor Activo/Autor Inactivo', default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    tipo = models.BooleanField('Administrador', default = False) 
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        
    def __str__(self):
        return "{0}, {1}".format(self.apellido, self.nombres)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Título', max_length= 150, blank=False, null=False)
    slug = models.CharField('Slug', max_length = 100, blank= False, null= False)
    descripcion = models.CharField('Descripción', max_length= 120, blank= False, null = False)
    contenido = RichTextField(default = "Contenido")
    imagen = models.URLField('Imagen', max_length=500, blank = True, null= True)
    autor = models.ForeignKey(Autor, on_delete= models.CASCADE)
    categoria = models.ForeignKey(Categorias, on_delete= models.CASCADE)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now= False, auto_now_add=True)
    estado = models.BooleanField('Publicado/No Publicado', default=True)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posteos'
        
    def __str__(self):
        return self.titulo
    

class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Título', max_length= 150, blank=False, null=False)
    contenido = models.TextField('Comentario', max_length= 800, blank= False, null = False)
    autor_id = models.ForeignKey(Autor, on_delete= models.CASCADE)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now= False, auto_now_add=True)


    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        
    def __str__(self):
        return self.titulo
    
    