"""Blog_info URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from blog.views import detalles_post, Inicio, ListarPost, crear_post, nuevo_usuario, Login, registrarse, listar_categorias, buscar_post, comentar
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path ('login/', Login.as_view(), name = 'login'),
    path('admin/', admin.site.urls),
    path('', ListarPost.as_view(), name = 'inicio'),
    path('postear/', login_required(crear_post), name= 'postear'),
    path('buscar/', buscar_post, name= 'buscar_post' ),
    path('registrarse/',nuevo_usuario, name ='registrarse'),
    path('categorias/', listar_categorias, name='lista_categorias'),
    path('<int:id>/', detalles_post, name = 'detalle_post'),
    path('<int:id>/comentar', comentar, name = 'comentar')
]
