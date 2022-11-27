from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import LivrosModel

from catalog.forms import AdicionarLivroForm, AtualizarLivroForm


# Create your views here.
def index(request):
    num_livros = LivrosModel.objects.all().count()
    
    context = {
        'num_livros': num_livros
    }
    
    return render(request, 'index.html', context=context)


def adicionar_livros(request):
    
    form = AdicionarLivroForm(request.POST)
    
    if request.method == 'POST':
        
        if form.is_valid():
            livros = LivrosModel()
            livros.nome = form.cleaned_data['nome']
            livros.autor = form.cleaned_data['autor']
            livros.preco = form.cleaned_data['preco']
            livros.save(livros)
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('livros'))
            
    context = {
        'form': form
    }

    return render(request, 'catalog/livros_add.html', context)

def editar_livro(request, id):
    
    livro = get_object_or_404(LivrosModel, id=id)

    form = AtualizarLivroForm(request.POST)
    
    if request.method == 'POST':
        
        if form.is_valid():
            livro.nome = form.cleaned_data['nome']
            livro.autor = form.cleaned_data['autor']
            livro.preco = form.cleaned_data['preco']
            livro.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('livros'))

    context = {
        'form': form,
        'livro_data': livro
    }
    
    return render(request, 'catalog/livros_editar.html', context)

def deletar_livro(request, id):
    livro = get_object_or_404(LivrosModel, id=id)
    livro.delete()
    return HttpResponseRedirect(reverse('livros'))

def listar_livros(request):
    livros = LivrosModel.objects.values()
    
    context = {
        'lista_livros': livros
    }
    
    return render(request, 'catalog/lista-de-livros.html', context=context)
            