from django import forms
from django.db.models import fields
from django.forms import widgets
from blog.models import Autor, Post, Categorias, Comentario


class AutorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Autor
        fields = ("__all__")
        widgets = { 'password': forms.PasswordInput()}
        
class CategoriasForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields =("__all__")
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("__all__")
        
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ("__all__")


class FiltroPost(forms.ModelForm):
    busqueda = forms.CharField(max_length=50, required=False)

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Autor
        fields = ('email',)
        widgets = { 'password': forms.PasswordInput()}