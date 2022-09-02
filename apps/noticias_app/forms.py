from django import forms
from django.forms import widgets
from .models import Noticia, Comentarios 

class NoticiaForm(forms.ModelForm):
    class Meta:
        model =  Noticia
        fields = ('autor','titulo','contenido', 'categorias')

        widget = {
            "titulo": forms.TextInput(attrs = {'class':'testInputClass'}),
            "conenido": forms.Textarea(attrs = {'class': 'editable medium-editor-textarea postcontent'}),
        }

class ComentarioForm(forms.Form):
    model = Comentarios
    fields = ('autor','cuerpo_comentario')

    autor = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Ingrese su nombre"
            })
    )
    cuerpo_comentario = forms.CharField(widget=forms.Textarea(
        attrs={
            "class":"form-control comment-textarea",
            "id":"comment",
            "placeholder":"Dinos que piensas, dejanos un comentario."
        })
    )

