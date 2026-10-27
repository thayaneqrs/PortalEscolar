from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models.deletion import ProtectedError

from .models import Categoria, Tag, Noticia
from .forms import CategoriaForm, TagForm


# Página inicial
def inicio(request):
    noticias = Noticia.objects.select_related(
        'categoria'
    ).prefetch_related('tags').order_by('-data_criacao')

    return render(
        request,
        'noticias/inicio.html',
        {'noticias': noticias}
    )


# LISTAGEM DE CATEGORIAS
def lista_categorias(request):
    categorias = Categoria.objects.all().order_by('nome')

    return render(
        request,
        'noticias/categorias.html',
        {'categorias': categorias}
    )


# CADASTRO DE CATEGORIA
def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Categoria cadastrada com sucesso!'
            )
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()

    return render(
        request,
        'noticias/detalhe_categoria.html',
        {'form': form}
    )


# EDIÇÃO DE CATEGORIA
def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Categoria atualizada com sucesso!'
            )
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)

    return render(
        request,
        'noticias/detalhe_categoria.html',
        {'form': form, 'categoria': categoria}
    )


# EXCLUSÃO DE CATEGORIA
def excluir_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)

    if request.method == 'POST':
        try:
            categoria.delete()
            messages.success(
                request,
                'Categoria excluída com sucesso!'
            )
        except ProtectedError:
            messages.error(
                request,
                'Não é possível excluir esta categoria, '
                'pois existem notícias vinculadas a ela.'
            )

        return redirect('lista_categorias')

    return render(
        request,
        'noticias/confirmar_exclusao_categoria.html',
        {'categoria': categoria}
    )


# LISTAGEM DE TAGS
def lista_tags(request):
    tags = Tag.objects.all().order_by('titulo')

    return render(
        request,
        'noticias/tags.html',
        {'tags': tags}
    )


# CADASTRO DE TAG
def cadastrar_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Tag cadastrada com sucesso!'
            )
            return redirect('lista_tags')
    else:
        form = TagForm()

    return render(
        request,
        'noticias/detalhe_tag.html',
        {'form': form}
    )


# EDIÇÃO DE TAG
def editar_tag(request, id):
    tag = get_object_or_404(Tag, pk=id)

    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Tag atualizada com sucesso!'
            )
            return redirect('lista_tags')
    else:
        form = TagForm(instance=tag)

    return render(
        request,
        'noticias/detalhe_tag.html',
        {'form': form, 'tag': tag}
    )


# EXCLUSÃO DE TAG
def excluir_tag(request, id):
    tag = get_object_or_404(Tag, pk=id)

    if request.method == 'POST':
        tag.delete()

        messages.success(
            request,
            'Tag excluída com sucesso!'
        )

        return redirect('lista_tags')

    return render(
        request,
        'noticias/confirmar_exclusao_tag.html',
        {'tag': tag}
    )