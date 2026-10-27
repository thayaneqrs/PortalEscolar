from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Tag(models.Model):
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='noticias'
    )

    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='noticias'
    )

    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo