"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name = 'home'),
    path('Nosotros/', views.Nosotros, name = 'nosotros'),
    path('Mision/',views.Mision, name = 'mision'),
    path('Galeria/',views.Galeria, name = 'galeria'),


#   NO OLVIDAR COMA AL FINAL DE CADA URL, ES UNA TUPLA

#LOGIN
    path('login/',auth.LoginView.as_view(template_name='usuarios/login.html'),name='login'),
    path('logout/',auth.LogoutView.as_view(),name="logout"),


# URL DE APLICACIONES
    path('Noticias/', include('apps.noticias.urls')),
    path('Usuario/',include('apps.usuarios.urls')),





    
]