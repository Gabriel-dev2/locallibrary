from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import LivrosModel

class AtualizarLivroForm(forms.Form):
    nome = forms.CharField(help_text="Entre um novo nome de livro")
    autor = forms.CharField(help_text="Entre um novo nome do autor")
    preco = forms.DecimalField(help_text="Entre um novo preço para o livro")
    
    def cleaned_data(self):
        nome = self.cleaned_data['nome']
        autor = self.cleaned_data['autor']
        preco = self.cleaned_data['preco']
        
        if nome is None:
            raise ValidationError(_('Nome precisa ser preenchido'))
        
        if autor is None:
            raise ValidationError(_('Autor precisa ser preenchido'))
        
        if preco is None:
            raise ValidationError(_('Preço precisa ser preenchido'))
        
        data = {
            'nome': nome,
            'autor': autor,
            'preco': preco
        }
        
        return data

class AdicionarLivroForm(forms.Form):
    nome = forms.CharField(help_text="Entre o nome de livro")
    autor = forms.CharField(help_text="Entre o nome do autor")
    preco = forms.DecimalField(help_text="Entre o preço do livro")
    
    def cleaned_data(self):
        nome = self.cleaned_data['nome']
        autor = self.cleaned_data['autor']
        preco = self.cleaned_data['preco']
        
        if nome is None:
            raise ValidationError(_('Nome precisa ser preenchido'))
        
        if autor is None:
            raise ValidationError(_('Autor precisa ser preenchido'))
        
        if preco is None:
            raise ValidationError(_('Preço precisa ser preenchido'))
        
        data = {
            'nome': nome,
            'autor': autor,
            'preco': preco
        }
        
        return data