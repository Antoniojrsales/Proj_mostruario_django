import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from app_mostruario.models import Produto

@pytest.fixture
def produto_ficticio(db):
    # Cria e devolve o produto apenas com os campos obrigatórios do seu model
    produto = Produto.objects.create(
        nome="Produto de Teste",
        preco=99.90,
        tag="normal"
        # Não enviamos imagem pois o model permite null=True e blank=True
    )
    return produto

@pytest.mark.django_db
def test_rota_lojinha_retorna_status_200_e_template_correto(client):
    # 1. Arrange (Preparação): Definimos que a rota se chamará 'lojinha_home'
    url = reverse('lojinha_home')
    
    # 2. Act (Ação): Simulamos um usuário acessando a URL
    response = client.get(url)
    
    # 3. Assert (Verificação): 
    # Garantimos que a resposta é 200 (OK) e não 404 (Not Found) ou 500 (Erro)
    assert response.status_code == 200
    
    # Garantimos que o Django escolheu o template HTML correto para renderizar
    templates_usados = [t.name for t in response.templates]
    assert 'app_mostruario/pages/lojinha.html' in templates_usados

@pytest.mark.django_db
def test_login_lojista_com_credenciais_validas(client):
    # 1. Arrange: Criamos um lojista virtual na base de dados de teste
    User.objects.create_user(username='admin', password='senha_segura_123')
    
    # 2. Act: Simulamos o envio do formulário (POST) que configurou no modal
    url = reverse('login_lojista')
    dados_login = {
        'username': 'admin',
        'password': 'senha_segura_123'
    }
    response = client.post(url, dados_login)
    
    # 3. Assert: Um login com sucesso no Django costuma redirecionar a página (Status 302)
    assert response.status_code == 302

@pytest.mark.django_db
def test_lojista_consegue_cadastrar_produto_via_modal(client):
    # 1. Arrange: Criamos um lojista e forçamos o login no cliente de testes
    user = User.objects.create_user(username='dono_loja', password='123')
    client.force_login(user)
    
    # 2. Act: Simulamos o POST do formulário para uma rota que AINDA NÃO EXISTE
    url = reverse('cadastrar_produto')
    dados_produto = {
        'nome': 'Kit Relação Dominator Titan 150',
        'preco': '84.90',
        'tag': 'mais_vendidos'
        # Vamos omitir a imagem neste primeiro teste pois definimos null=True, blank=True
    }
    response = client.post(url, dados_produto)
    
    # 3. Assert: Esperamos um redirecionamento (302) e que o produto esteja salvo no BD
    assert response.status_code == 302
    assert Produto.objects.count() == 1
    assert Produto.objects.first().nome == 'Kit Relação Dominator Titan 150'

@pytest.mark.django_db
def test_lojista_consegue_fazer_logout(client):
    # 1. Arrange: Criamos um utilizador e forçamos o login ativo
    user = User.objects.create_user(username='dono_loja_sair', password='123')
    client.force_login(user)
    
    # 2. Act: Tentamos chamar a rota de logout que ainda não criámos
    url = reverse('logout_lojista')
    response = client.get(url)
    
    # 3. Assert: Esperamos um redirecionamento (302) e a perda da sessão (is_authenticated == False)
    from django.contrib.auth import get_user
    assert response.status_code == 302
    assert not get_user(client).is_authenticated

@pytest.mark.django_db
def test_home_envia_produtos_de_destaque_para_o_carrossel(client):
    # 1. Arrange: Criamos um produto destaque e um normal para garantir que o filtro da view funciona
    Produto.objects.create(nome="Kit Destaque", preco="80.00", tag="destaque_semana")
    Produto.objects.create(nome="Capa Normal", preco="50.00", tag="normal")
    
    # 2. Act: Acessamos a rota da página inicial
    url = reverse('lojinha_home')
    response = client.get(url)
    
    # 3. Assert: Validamos o status e o que foi enviado para o HTML
    assert response.status_code == 200
    
    # Capturamos a variável 'destaques' que a nossa view envia para o template
    destaques = response.context.get('destaques')
    
    assert destaques is not None
    assert len(destaques) == 1
    assert destaques[0].nome == "Kit Destaque"

@pytest.mark.django_db
def test_home_separa_produtos_por_categoria_para_o_catalogo(client):
    # 1. Arrange: Criamos um produto para cada tag do catálogo
    Produto.objects.create(nome="Kit Padrão", preco="50.00", tag="normal")
    Produto.objects.create(nome="Capa Sucesso", preco="120.00", tag="mais_vendidos")
    Produto.objects.create(nome="Luva Barata", preco="30.00", tag="promocao")
    
    # 2. Act: Acedemos à view principal
    url = reverse('lojinha_home')
    response = client.get(url)
    
    # 3. Assert: Validamos se a view devolve as listas separadas no contexto
    assert response.status_code == 200
    
    normais = response.context.get('produtos_normais')
    mais_vendidos = response.context.get('produtos_mais_vendidos')
    promocoes = response.context.get('produtos_promocoes')
    
    # Verificamos se as listas existem e contêm exatamente 1 produto cada
    assert normais is not None and len(normais) == 1
    assert mais_vendidos is not None and len(mais_vendidos) == 1
    assert promocoes is not None and len(promocoes) == 1
    
    # Garantimos que a view não misturou os produtos nas categorias erradas
    assert normais[0].nome == "Kit Padrão"
    assert mais_vendidos[0].nome == "Capa Sucesso"
    assert promocoes[0].nome == "Luva Barata"

@pytest.mark.django_db
def test_editar_produto_requer_autenticacao(client, produto_ficticio):
    # A rota 'editar_produto' ainda será criada no urls.py
    url = reverse('editar_produto', kwargs={'id': produto_ficticio.id})
    resposta = client.get(url)
    
    # Espera-se um redirecionamento (302) para a página de login
    assert resposta.status_code == 302
    assert '/login' in resposta.url

@pytest.mark.django_db
def test_excluir_produto_requer_autenticacao(client, produto_ficticio):
    url = reverse('excluir_produto', kwargs={'id': produto_ficticio.id})
    resposta = client.post(url)
    
    assert resposta.status_code == 302
    assert '/login' in resposta.url

@pytest.mark.django_db
def test_lojista_consegue_editar_produto(client, produto_ficticio, django_user_model):
    # 1. Criar e autenticar o lojista
    lojista = django_user_model.objects.create_user(username='lojista_teste', password='123')
    client.force_login(lojista)
    
    # 2. Dados atualizados do formulário
    novos_dados = {
        'nome': 'Capacete Editado',
        'preco': '150.00',
        'tag': 'promocao'
    }
    
    # 3. Enviar requisição POST para atualizar
    from django.urls import reverse
    url = reverse('editar_produto', kwargs={'id': produto_ficticio.id})
    resposta = client.post(url, novos_dados)
    
    # 4. Validar o redirecionamento (302) e a alteração na base de dados
    assert resposta.status_code == 302
    produto_ficticio.refresh_from_db()
    assert produto_ficticio.nome == 'Capacete Editado'
    assert float(produto_ficticio.preco) == 150.00

@pytest.mark.django_db
def test_lojista_consegue_excluir_produto(client, produto_ficticio, django_user_model):
    lojista = django_user_model.objects.create_user(username='lojista_teste2', password='123')
    client.force_login(lojista)
    
    url = reverse('excluir_produto', kwargs={'id': produto_ficticio.id})
    resposta = client.post(url)
    
    assert resposta.status_code == 302
    
    # Validar se o produto desapareceu da base de dados
    from app_mostruario.models import Produto
    assert Produto.objects.count() == 0

@pytest.mark.django_db
def test_adicionar_produto_ao_carrinho_via_sessao(client, produto_ficticio):
    from django.urls import reverse
    
    # 1. Definimos a futura rota que processará o clique
    url = reverse('adicionar_carrinho', kwargs={'id': produto_ficticio.id})
    
    # 2. Simulamos o clique no botão "Adicionar ao carrinho" (requisição POST)
    resposta = client.post(url)
    
    # 3. Esperamos que o sistema adicione e redirecione de volta para a montra (302)
    assert resposta.status_code == 302
    
    # 4. Inspecionamos a sessão do navegador simulado
    carrinho = client.session.get('carrinho', {})
    
    # O JSON da sessão guarda as chaves do dicionário sempre como strings
    produto_id_str = str(produto_ficticio.id)
    
    # Validamos as regras de negócio de segurança e dados
    assert produto_id_str in carrinho
    assert carrinho[produto_id_str]['quantidade'] == 1
    assert carrinho[produto_id_str]['preco'] == '99.90' # Valor exato da nossa fixture

@pytest.mark.django_db
def test_adicionar_produto_inexistente_retorna_404(client):
    from django.urls import reverse
    # Tenta adicionar um ID que não existe na base de dados
    url = reverse('adicionar_carrinho', kwargs={'id': 9999})
    resposta = client.post(url)
    
    # O sistema deve barrar a ação imediatamente com um Not Found
    assert resposta.status_code == 404

@pytest.mark.django_db
def test_incremento_de_quantidade_e_integridade_no_carrinho(client, produto_ficticio):
    from django.urls import reverse
    url = reverse('adicionar_carrinho', kwargs={'id': produto_ficticio.id})
    
    # Simula o utilizador a clicar duas vezes no botão "Adicionar"
    client.post(url)
    client.post(url)
    
    carrinho = client.session.get('carrinho', {})
    produto_id_str = str(produto_ficticio.id)
    
    # A quantidade deve ser exatamente 2 (não pode duplicar o item nem manter 1)
    assert carrinho[produto_id_str]['quantidade'] == 2
    # O preço injetado tem de continuar a ser estritamente o da base de dados
    assert carrinho[produto_id_str]['preco'] == '99.90'

@pytest.mark.django_db
def test_remover_produto_do_carrinho(client, produto_ficticio):
    from django.urls import reverse
    
    # 1. Adiciona o produto ao carrinho
    url_add = reverse('adicionar_carrinho', kwargs={'id': produto_ficticio.id})
    client.post(url_add)
    
    # 2. Confirma que ele entrou na sessão
    assert str(produto_ficticio.id) in client.session.get('carrinho', {})
    
    # 3. Dispara o clique no futuro botão de remover
    url_remover = reverse('remover_carrinho', kwargs={'id': produto_ficticio.id})
    client.post(url_remover)
    
    # 4. Exige que a sessão não contenha mais esse ID
    assert str(produto_ficticio.id) not in client.session.get('carrinho', {})

@pytest.mark.django_db
def test_geracao_link_whatsapp_no_context_processor(client, produto_ficticio):
    from django.urls import reverse
    import urllib.parse
    
    # 1. Injetamos um cenário controlado diretamente na sessão do navegador de teste
    session = client.session
    session['carrinho'] = {
        str(produto_ficticio.id): {
            'nome': produto_ficticio.nome,
            'preco': '150.00', # Valor fixo para o teste
            'quantidade': 2
        }
    }
    session.save()
    
    # 2. Fazemos um GET à página inicial (que aciona os context_processors)
    resposta = client.get(reverse('lojinha_home'))
    
    # 3. Capturamos a variável global que deve ter sido gerada
    link_gerado = resposta.context.get('link_whatsapp')
    
    # A variável tem de existir e não pode ser apenas o sustenido "#"
    assert link_gerado is not None
    assert link_gerado != "#"
    
    # 4. Descodificamos o URL para conseguirmos ler o texto limpo
    texto_legivel = urllib.parse.unquote(link_gerado)
    
    # 5. Validações estritas de negócio
    assert "5585992049066" in texto_legivel  # O número do lojista está correto
    assert produto_ficticio.nome in texto_legivel  # O nome do produto aparece na lista
    assert "300,00" in texto_legivel  # O total (150 * 2) foi devidamente calculado e formatado