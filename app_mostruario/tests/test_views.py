import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from app_mostruario.models import Produto

# Marcação necessária para o pytest saber que este teste pode interagir com o Django
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