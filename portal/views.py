from django.shortcuts import render, get_object_or_404
from .models import Menu, Conteudo

# Função auxiliar para buscar o menu dinâmico
# Será usada em todas as páginas para o menu aparecer sempre
def get_menu_context():
    return {'menu_itens': Menu.objects.filter(ativo=True)}


def home(request):
    # Página inicial
    context = get_menu_context()
    context['pagina_atual'] = 'Início'
    return render(request, 'portal/home.html', context)


def conteudo_detalhe(request, slug):
    # Página de um conteúdo específico (ex: /conteudo/meu-tema/)
    context = get_menu_context()
    
    # Busca o conteúdo pelo slug. Se não existir, retorna erro 404
    conteudo = get_object_or_404(Conteudo, slug=slug, ativo=True)
    
    context['conteudo'] = conteudo
    return render(request, 'portal/conteudo_detalhe.html', context)
