#from xml.etree.ElementTree import Comment
from time import timezone
from django.shortcuts import render, redirect
from .models import Noticia,Categoria,Comentarios
from django.http.response import Http404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import NoticiaForm, ComentarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView)
#from django.http import HttpResponse

# Create your views here.

def index(request):
    #texto = {'mensaje_texto': 'Esta es mi primer pagina :)'}
    ultimasnoticias = Noticia.objects.all().order_by('creado').reverse()[:2]
    context ={
        'noticiasdestacadas':ultimasnoticias
    }
    return render(request, 'index.html',context)
    

def eventos(request):
    return render(request, 'eventos.html', {})

def misionVision(request):
    return render(request, 'mision-vision.html', {})

def noticias(request):
    lista_noticias = Noticia.objects.all().order_by('creado')
    context = {
        "noticias": lista_noticias,
        "MEDIA_ROOT": 'img/noticias/'
    }
    return render(request, 'noticias.html',context)

def noticiasdetalle(request, id):
    try:
        datanoticia = Noticia.objects.get(id=id)
        lista_comentarios = Comentarios.objects.filter(aprobado=True)
    except Noticia.DoesNotExist:
        raise Http404('La noticia solicitada no existe')

    form = ComentarioForm()
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            print("Validación Exitosa!!")
            print("Autor:" + form.cleaned_data["autor"])
            print("Comentario" + form.cleaned_data["cuerpo_comentario"])
            comment = Comentarios(
                autor = form.cleaned_data["autor"],
                comment_body = form.cleaned_data ["cuerpo_comentario"],
                noticias = datanoticia
            )
            comment.save()
            
    context = {
        "noticia": datanoticia,
        "comentarios": lista_comentarios,
        "formulario_comentario": form,
        "MEDIA_ROOT": 'media/img/noticias/'
    }
    return render(request, 'detalle-noticia.html',context)   

class CrearNoticiaView(CreateView, LoginRequiredMixin):
    login_url = '/login'
    form_class = NoticiaForm
    model = Noticia


    def blog_categoria(request, categoria):
        posts = Noticia.objects.filter(categories__name__contains=categoria).order_by('creado')
        context = {
            "categoria": categoria,
            "posts": posts
        }
        return render(request, "blog_categoria.html", context)


def quienesSomos(request):
    return render(request, 'quienes-somos.html', {})

def programaRadio(request):
    return render(request, 'programaRadio.html', {})

def contacto(request):
    return render(request, 'contacto.html', {})

def login(request):
    return render(request, 'login.html', {})


@login_required
def comment_approve(request, id):
    try:
        comentarios=Comentarios.objects.get(id=id)
    except Comentarios.DoesNotExist:
        raise Http404('El comentario no existe')
    comentarios.approve()
    return redirect('noticiasdetalle', id = comentarios.noticia.id)
    
@login_required
def comment_remove(request, id):
    try:
        comentarios=Comentarios.objects.get(id=id)
    except Comentarios.DoesNotExist:
        raise Http404('El comentario no existe')
    comentarios.delete()
    return redirect('noticiasdetalle', id = comentarios.noticia.id)   

@login_required
def post_publish(request, id):
    try:
        noticias =Noticia.objects.get(id =id)
    except Noticia.DoesNotExist:
        raise Http404('No existe la noticia')
    
    Noticia.publish()
    return redirect('noticiasdetalle', id=id)