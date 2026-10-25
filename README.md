# 🛒 Projeto: Page Mostruario - E-commerce & Catálogo Dinâmico

Plataforma de e-commerce interativa focada em performance e experiência do utilizador (UX). Desenvolvida com Django, Bootstrap 5 e JavaScript, a aplicação gere um catálogo completo com filtros de texto e categoria em tempo real, paginação via front-end e redirecionamento de conversão para o WhatsApp. A arquitetura back-end utiliza PostgreSQL para assegurar a integridade relacional do inventário e das operações de gestão de produtos.

## ✅ Etapas de Inicialização

- Estruturação do projeto em pastas
- Criação do ambiente virtual
- Definição das bibliotecas principais (via `requirements.txt`)
- Configuração do `.gitignore`
- Primeiros arquivos adicionados ao controle de versão

## 📁 Estrutura Inicial de Pastas

```
Proj_mostruario_django/
├── app_mostruario/
│   ├── domain  
│       └── __init__.py
│       └── selectors.py
│       └── services.py
│   ├── migrations
│   ├── static
│       ├── app_mostruario
│           ├── css
│           ├── js
│   ├── templates
│       ├── app_mostruario
│           ├── pages 
│               └── lojinha.html
│           ├── partials
│               └── footer.html
│               └── head.html
│               └── navbar.html
│   ├── tests
│       └── __init__.py
│       └── test_views.py
│   └── __init__.py
│   └── admin.py
│   └── apps.py
│   └── models.py
│   └── views.py
├── base_templates/
│   ├── global
│       └── base.html  
├── core/
│   └── __init__.py   
│   └── asgi.py       
│   └── settings.py          
│   └── urls.py
│   └── wsgi.py    
├── db_data/
├── media/
├── straticfiles/
├── venv/
└── .env
├── .gitignore
└── docker-compose.yml
└── Dockerfile
└── LICENSE
└── manage.py
└── pytest.ini
├── README.md
└── requirements.txt
```

## ✨ Funcionalidades Principais

| Recurso | Descrição | Habilidades Demonstradas |
| :--- | :--- | :--- |
| **Catálogo Dinâmico** | Renderização de produtos a partir da base de dados com limite de exibição e paginação visual (Botão "Ver Mais"). | Django ORM, PostgreSQL, Integração Back-end/Front-end. |
| **Filtros em Tempo Real** | Busca instantânea por texto e categorização por abas sem recarregamento da página, poupando processamento no servidor. | JavaScript (Manipulação de DOM), Lógica de Otimização (UX). |
| **Cadastro de Produtos** | Inserção de novos itens no inventário via modal front-end com persistência direta na base de dados. | Django Views, Tratamento de POST, Segurança CSRF. |
| **Conversão Direta (FAB)** | Botão flutuante de WhatsApp ancorado na interface para facilitar o contacto imediato do cliente. | UX/UI Design, Bootstrap 5 (Classes Utilitárias). |

## 🛠 Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes ferramentas e bibliotecas:

* **Back-end:** Python 3.x, Django (Arquitetura MVT), Pillow (Processamento e manipulação das imagens do catálogo).
* **Front-end:** HTML5, CSS3, JavaScript (Manipulação de DOM e Eventos), Bootstrap 5.
* **Base de Dados:** PostgreSQL, Django ORM.
* **Testes & Qualidade:** Pytest (Test-Driven Development para validação de regras de negócio e rotas).
* **Ambiente & Ferramentas:** Docker (Testes e isolamento), Git/GitHub.

## 🚀 Como Executar o Projeto Localmente

Pré-requisitos: É necessário ter o [Docker](https://www.docker.com/) e o [Docker Compose](https://docs.docker.com/compose/) instalados no sistema.

**1. Clonar o repositório**
```bash
git clone [https://github.com/Antoniojrsales/Proj_mostruario_django.git]
(https://github.com/Antoniojrsales/Proj_mostruario_django)
cd nome-do-repositorio

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

**2. Iniciar os contentores Docker**
docker-compose up --build -d

**3. Aplicar as migrações no PostgreSQL**
docker-compose exec web python manage.py migrate

**4. Criar o utilizador gestor (Opcional)**
docker-compose exec web python manage.py createsuperuser

**5. Correr a suite de testes (Pytest)**
docker-compose exec web pytest

```
A aplicação ficará disponível no navegador através do endereço http://localhost:8000.
```