# ATV09 - Migração do Portal para Django

## Identificação da Dupla
- **Aluno 1:** Luiz Philippe de Lima Silva
- **Aluno 2:** Miguel Barbosa Neto
- **Aluno 3:** Manoel Fernando Cavalcante Cruz
- **Turma:** 513

## Descrição do Projeto
Migração do portal acadêmico desenvolvido na ATV06 para o framework Django. O projeto mantém a identidade visual, estrutura responsiva e organização semântica da ATV06, adicionando funcionalidades dinâmicas através do Django Admin.

## Tecnologias Utilizadas
- Python 3.12
- Django 6.1.2
- HTML5
- CSS3 (Flexbox)
- SQLite3 (banco de dados padrão do Django)
- Git e GitHub

## Estrutura do Projeto

    ATV09_NOME1_NOME2/
    ├── core/                  # Configurações do projeto Django
    ├── portal/                # Aplicação principal
    │   ├── migrations/        # Migrations do banco de dados
    │   ├── models.py          # Models Conteudo e Menu
    │   ├── views.py           # Views da aplicação
    │   ├── urls.py            # URLs da aplicação
    │   └── admin.py           # Configuração do Django Admin
    ├── templates/             # Templates HTML
    │   └── portal/
    │       ├── base.html
    │       ├── home.html
    │       └── conteudo_detalhe.html
    ├── static/                # Arquivos estáticos
    │   ├── css/
    │   │   └── style.css
    │   └── img/
    ├── manage.py
    ├── db.sqlite3
    └── requirements.txt

## Instruções de Instalação e Execução

### 1. Clonar o Repositório

    git clone <URL_DO_REPOSITORIO>
    cd ATV09_NOME1_NOME2

### 2. Criar Ambiente Virtual

    python -m venv venv

### 3. Ativar Ambiente Virtual

**Windows:**

    .\venv\Scripts\activate

**Linux/Mac:**

    source venv/bin/activate

### 4. Instalar Dependências

    pip install -r requirements.txt

### 5. Executar Migrations

    python manage.py migrate

### 6. Criar Superusuário

    python manage.py createsuperuser

Digite o username, email (opcional) e senha quando solicitado.

### 7. Executar o Servidor

    python manage.py runserver

## Acessos

### Aplicação
- **URL:** http://127.0.0.1:8000/
- Página inicial do portal com navegação dinâmica

### Django Admin
- **URL:** http://127.0.0.1:8000/admin/
- Login com as credenciais do superusuário criado
- Permite cadastrar, alterar, excluir e ativar/desativar conteúdos e itens do menu

## Funcionalidades Implementadas

### Models
- **Conteudo:** Armazena os conteúdos do portal (título, slug, conteúdo HTML, ativo)
- **Menu:** Representa os itens de navegação (título, tipo destino, ordem, ativo, relacionamento com Conteudo ou URL externa)

### Menu Dinâmico
O menu é gerado automaticamente a partir dos registros do Model Menu no banco de dados. Não é necessário alterar o template para adicionar, remover ou reordenar itens.

### URLs Dinâmicas
- `/` - Página inicial
- `/conteudo/<slug>/` - Exibição de conteúdo específico (ex: `/conteudo/curriculo-luiz/`)

### Arquivos Estáticos
- CSS organizado em `static/css/`
- Imagens organizadas em `static/img/`
- Referenciados corretamente nos templates e conteúdos HTML

### Responsividade
Mantidas todas as características responsivas da ATV06:
- Meta viewport configurado
- Flexbox para layout
- Media queries para adaptação mobile
- Imagens responsivas

## Conteúdo Mínimo Implementado
-  1 página inicial
-  6 conteúdos internos (Currículos e Temas Livres dos 3 integrantes)
-  1 link externo (GitHub)

## Versionamento
Projeto versionado com Git e disponibilizado no GitHub com histórico de commits demonstrando o desenvolvimento da atividade.