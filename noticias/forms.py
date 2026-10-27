from django import forms
from .models import Categoria, Tag


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        labels = {
            'nome': 'Nome da categoria',
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome', '')

        if not nome.strip():
            raise forms.ValidationError(
                'O nome da categoria é obrigatório.'
            )

        return nome.strip()


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['titulo']
        labels = {
            'titulo': 'Nome da tag',
        }

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo', '')

        if not titulo.strip():
            raise forms.ValidationError(
                'O nome da tag é obrigatório.'
            )

        return titulo.strip()