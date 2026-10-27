from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),

    # Categorias
    path(
        'categorias/',
        views.lista_categorias,
        name='lista_categorias'
    ),
    path(
        'categorias/nova/',
        views.cadastrar_categoria,
        name='cadastrar_categoria'
    ),
    path(
        'categorias/<int:id>/editar/',
        views.editar_categoria,
        name='editar_categoria'
    ),
    path(
        'categorias/<int:id>/excluir/',
        views.excluir_categoria,
        name='excluir_categoria'
    ),

    # Tags
    path(
        'tags/',
        views.lista_tags,
        name='lista_tags'
    ),
    path(
        'tags/nova/',
        views.cadastrar_tag,
        name='cadastrar_tag'
    ),
    path(
        'tags/<int:id>/editar/',
        views.editar_tag,
        name='editar_tag'
    ),
    path(
        'tags/<int:id>/excluir/',
        views.excluir_tag,
        name='excluir_tag'
    ),
]