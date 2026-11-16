# Antonio Gomes Sales Junior
# Plano B
# 🛒 Projeto: Page Mostruario - E-commerce & Catálogo Dinâmico

Plataforma de e-commerce interativa focada em performance e experiência do utilizador (UX). Desenvolvida com Django, Bootstrap 5 e JavaScript, a aplicação gere um catálogo completo com filtros de texto e categoria em tempo real, paginação via front-end e redirecionamento de conversão para o WhatsApp. A arquitetura back-end utiliza PostgreSQL para assegurar a integridade relacional do inventário e das operações de gestão de produtos.

## 🏗️ Padrão Arquitetural: Django MVT (Model-View-Template)

Para o desenvolvimento deste projeto, optou-se pela utilização do framework Django com o seu padrão nativo **MVT** e o ORM baseado em **Active Record**. 

**Justificativa Técnica:**
1. **Velocidade de Entrega (Time-to-Market):** O forte acoplamento entre os Models (PostgreSQL) e as Views/Templates permitiu o desenvolvimento rápido do catálogo e do motor de carrinho baseado em sessões, sem a sobrecarga de construir e manter uma API REST/GraphQL separada para o Front-End nesta fase.
2. **Coesão e Manutenção:** Manter o fluxo de dados centralizado num Monólito reduz a complexidade de infraestrutura e facilita o deploy contínuo (via Docker Compose).

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
| **API & OpenAPI (Swagger)** | Exposição de catálogo via endpoint JSON e documentação interativa gerada dinamicamente. | Django Ninja, RESTful API, Serialização de Dados. |

## 🛠 Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes ferramentas e bibliotecas:

* **Back-end:** Python 3.x, Django (Arquitetura MVT), Pillow (Processamento e manipulação das imagens do catálogo).
* **Front-end:** HTML5, CSS3, JavaScript (Manipulação de DOM e Eventos), Bootstrap 5.
* **Base de Dados:** PostgreSQL, Django ORM.
* **Qualidade de Código & Testes:** Pytest, pytest-cov, Flake8 (Linting).
* **DevOps & Infraestrutura:** Docker, Docker Compose, GitHub Actions (CI/CD).

## ⚙️ Integração Contínua (CI/CD) e Testes

O projeto conta com uma esteira de Integração Contínua configurada via **GitHub Actions** (`.github/workflows/ci.yml`). A cada *push* ou *pull request* para a *branch* principal, a pipeline executa as seguintes validações:
1. Construção da infraestrutura isolada (Docker).
2. Análise estática de qualidade de código (Linting) com **Flake8**.
3. Execução da suite de testes automatizados com **Pytest**.

**Cobertura de Testes (Coverage):**
A suite de testes utiliza o padrão *Arrange-Act-Assert* e garante a integridade das regras de negócio, carrinho de compras e segurança das rotas. O projeto possui atualmente **93% de cobertura de código**.

## 📊 Observabilidade e Performance

A aplicação foi instrumentada para garantir total observabilidade em ambientes de produção:

* **Métricas (Prometheus):** Integração com `django-prometheus` para exposição de métricas de consumo de memória, latência de requisições HTTP e operações no banco de dados.
* **Logs Estruturados:** Utilização da biblioteca `django-structlog` para padronizar as saídas do terminal em formato JSON, facilitando a ingestão por ferramentas modernas de monitorização (ELK Stack, Datadog, etc.).

### ⚡ Teste de Carga e Stress (k6)
Para validar a resiliência da arquitetura, o projeto foi submetido a testes de carga utilizando o **Grafana k6**. 
O cenário simulou o acesso simultâneo de **50 utilizadores virtuais (VUs)** às rotas de renderização HTML e à API REST durante 1 minuto e 40 segundos, resultando em:
* **Total de Requisições:** 4.280 efetuadas com sucesso.
* **Taxa de Erro:** 0.00% (Zero falhas no processamento).
* **Latência:** Tempo de resposta estável e sem gargalos na base de dados PostgreSQL sob stress.

## 🚀 Como Executar o Projeto Localmente

Pré-requisitos: É necessário ter o [Docker](https://www.docker.com/) e o [Docker Compose](https://docs.docker.com/compose/) instalados no sistema.

**1. Clonar o repositório**
```bash
git clone [https://github.com/Antoniojrsales/Proj_mostruario_django.git](https://github.com/Antoniojrsales/Proj_mostruario_django)
cd nome-do-repositorio
cp .env.example .env

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

**2. Iniciar a infraestrutura (Docker Compose):**
docker-compose up --build -d

**3. Aplicar as migrações no PostgreSQL:**
docker-compose exec web python manage.py migrate

**4. Criar o utilizador gestor (Opcional):**
docker-compose exec web python manage.py createsuperuser

**5. Correr a suite de testes (Pytest):**
docker-compose exec web pytest

## 🌐 Endpoints e Acesso

Com o projeto a correr localmente, pode aceder às seguintes rotas no seu navegador:

- **Aplicação Principal (Catálogo HTML):** [http://localhost:8000](http://localhost:8000)
- **Endpoint da API (Lista de Produtos em JSON):** [http://localhost:8000/api/produtos/](http://localhost:8000/api/produtos/)
- **Documentação Interativa (Swagger/OpenAPI):** [http://localhost:8000/api/docs](http://localhost:8000/api/docs)
- **Métricas da Aplicação (Prometheus):** [http://localhost:8000/metrics](http://localhost:8000/metrics)

## 🌍 Projeto em Produção (Live Demo)

A aplicação encontra-se atualmente em produção, hospedada no **Railway**, operando como uma vitrine digital real (ex: JR MOTOS). O ecossistema completo abrange tanto a experiência do cliente final como a gestão do lojista.
**Página Inicial e Carrossel:** Interface limpa com banner da loja e secção interativa de destaques, otimizando a visibilidade de produtos em oferta.
**Catálogo Dinâmico:** Listagem de produtos com barra de pesquisa e filtros rápidos em abas (Lançamentos, Mais Vendidos, Promoções).
<p align="center">
  <img width="1866" height="675" alt="home mostruario" src="https://github.com/user-attachments/assets/f20e36b5-954b-413f-ad06-b85babb959ae" />
  <img width="1877" height="595" alt="carrossel mostruario" src="https://github.com/user-attachments/assets/6e083191-07fa-4e2d-bc64-8d1eadb26f3f" />
  <img width="1891" height="932" alt="catalogo mostruario" src="https://github.com/user-attachments/assets/bda7af98-6235-4d90-88fa-37c213c55181" />
</p>
**Motor de Conversão (Carrinho):** Sistema de checkout em tempo real que calcula o total e redireciona o utilizador diretamente para fechar a compra via WhatsApp.
**Gestão do Lojista:** Modal de acesso restrito (autenticação segura) para a administração do inventário de forma simples e direta.
<p align="center">
  <img width="547" height="947" alt="fechar compras mostruario" src="https://github.com/user-attachments/assets/03ad465d-bf9a-4c2b-ae9f-f7309c9bb16b" />
  <img width="327" height="297" alt="area logista mostruario" src="https://github.com/user-attachments/assets/ae2c2f44-a1a6-4885-b3b9-8729384956d0" />
</p>
