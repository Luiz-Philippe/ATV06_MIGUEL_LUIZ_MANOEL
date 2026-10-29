from django.db import models

class Conteudo(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    conteudo_html = models.TextField()
    ativo =  models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class Menu(models.Model):
    TIPO_DESTINO = (
        ('INTERNO', 'Conteúdo Interno'),
        ('EXTERNO', 'Link Externo'),
    )
    
    titulo = models.CharField(max_length=100)
    tipo_destino = models.CharField(max_length=7, choices=TIPO_DESTINO)
    ordem = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)

    # Relacionamento com Conteudo (usado quando tipo_destino = INTERNO)
    conteudo = models.ForeignKey(
        Conteudo, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )

    # URL externa (usada quando tipo_destino = EXTERNO)
    url_externa = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return self.titulo