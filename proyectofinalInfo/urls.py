"""proyectofinalInfo URL Configuration

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
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import include,path
from django.urls import re_path as url
from django.conf.urls.static import static
from django.conf import settings
from apps.noticias_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('eventos/', views.eventos, name='eventos'),
    path('misionVision/', views.misionVision, name='misionVision'),
    path('noticias/', views.noticias, name='noticias'),    
    path('quienesSomos/', views.quienesSomos, name='quienesSomos'),
    path('programaRadio/', views.programaRadio, name='programaRadio'),
    path('contacto/', views.contacto, name='contacto'),
    path('registration/', include('apps.blog_auth.urls', namespace='apps.blog_auth')),
    url('noticias/', include('apps.noticias_app.urls', namespace='apps.noticias_app')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
