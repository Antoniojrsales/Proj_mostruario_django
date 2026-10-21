import pytest
from django.urls import reverse

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