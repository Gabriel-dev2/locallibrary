from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('livro/', views.listar_livros, name='livros'),
    path('livro', views.adicionar_livros, name='adicionar-livros'),
    path('livro/<int:id>/atualizar/', views.editar_livro, name='atualizar-livro'),
    path('livro/<int:id>/delete/', views.deletar_livro, name='deletar-livro'),
]

