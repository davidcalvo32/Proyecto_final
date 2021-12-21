from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .forms import *
from .models import Post, Categorias
from django.db.models import Q
from django.views.generic import View, ListView, TemplateView, UpdateView


class Inicio(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    
           
class Login(TemplateView):
    template_name = 'login.html'

class ListarPost(ListView):
    model = Post
    template_name = 'index.html'
    queryset = Post.objects.filter(estado=True)
    
def buscar_post(request):
    formulario = FiltroPost(request.Get or None)
    if formulario.is_valid():
        posts = Post.objects.filter(
        Q(titulo__icontains = formulario) |
        Q(descripcion__icontains = formulario) |
        Q(fecha_creacion__icontains = formulario)    
        ).distinct()
    
    return render(request, 'filtrar_post.html', {'posts':posts})

def crear_post(request):
    return render(request, 'crear_post.html')

def registrarse(request):
    return render(request, 'registrarse.html')

def nuevo_usuario(request):
    formulario = AutorForm(request.POST or None)
    
    if request.method == "POST":
        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")

    template = "registrarse.html"
    contexto = {
        "formulario_n":formulario
    }
    return render(request, template, contexto)
    

def listar_comentarios(request):
    pass

def listar_categorias(request):
    queryset = request.GET.get("buscar")
    categorias = Categorias.objects.filter(estado = True)
    if queryset:
        categorias = Categorias.objects.filter(
        Q(titulo__icontains = queryset) |
        Q(descripcion__icontains = queryset) |
        Q(fecha_creacion__icontains = queryset)    
        ).distinct()
    
    return render(request, 'listado_categorias.html', {'categorias':categorias})



def detalles_post(request, id):
    post = Post.objects.get(
        id = id
    )
    print (post)
    return render(request, 'post.html', {'detallepost': post})


def login_usuario(request):
    formulario = LoginForm(request.POST or None)
    
    if request.method == "POST":
        if formulario.is_valid():
            
            return redirect("inicio")

    template = "login.html"
    contexto = {
        "formulario_l":formulario
    }
    return render(request, template, contexto)

def comentar(request):
    formulario = ComentarioForm(request.POST or None)
    
    if request.method == "POST":
        if formulario.is_valid():
            formulario.save()
            return redirect("post.html")

    template = "post.html"
    contexto = {
        "formulario_c":formulario
    }
    return render(request, template, contexto)