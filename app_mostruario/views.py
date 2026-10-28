from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Produto
from django.contrib.auth.decorators import login_required

def lojinha_home(request):
    # O filtro do carrossel que já existia
    destaques = Produto.objects.filter(tag='destaque_semana')
    
    # Os novos filtros para as secções do catálogo
    produtos_normais = Produto.objects.filter(tag='normal')
    produtos_mais_vendidos = Produto.objects.filter(tag='mais_vendidos')
    produtos_promocoes = Produto.objects.filter(tag='promocao')
    
    # Empacotamento de todas as variáveis no contexto
    context = {
        'destaques': destaques,
        'produtos_normais': produtos_normais,
        'produtos_mais_vendidos': produtos_mais_vendidos,
        'produtos_promocoes': produtos_promocoes,
    }
    
    return render(request, 'app_mostruario/pages/lojinha.html', context)

def login_lojista(request):
    if request.method == 'POST':
        # Captura os dados enviados pelos atributos "name" do modal
        usuario = request.POST.get('username')
        palavra_passe = request.POST.get('password')
        
        # O Django verifica se o utilizador e a senha correspondem à base de dados
        user = authenticate(request, username=usuario, password=palavra_passe)
        
        if user is not None:
            login(request, user)
            # Redireciona de volta para a home após sucesso (o nosso teste espera este redirecionamento 302)
            return redirect('lojinha_home')
        else:
            # Mais tarde podemos adicionar uma mensagem de erro aqui, por agora volta à home
            return redirect('lojinha_home')
            
    # Se alguém tentar aceder via GET diretamente, redireciona para a home
    return redirect('lojinha_home')

def cadastrar_produto(request):
    if request.method == 'POST':
        # 1. Capturar os dados que vêm do atributo "name" do HTML
        nome_produto = request.POST.get('nome')
        preco_produto = request.POST.get('preco')
        tag_produto = request.POST.get('tag')
        
        # Para ficheiros (como imagens), usamos request.FILES em vez de request.POST
        imagem_produto = request.FILES.get('imagem') 
        
        # 2. Criar o registo na base de dados
        Produto.objects.create(
            nome=nome_produto,
            preco=preco_produto,
            tag=tag_produto,
            imagem=imagem_produto
        )
        
        # 3. Redirecionar de volta para a página principal (o 302 que o teste espera)
        return redirect('lojinha_home')
        
    return redirect('lojinha_home')

def logout_lojista(request):
    logout(request)
    return redirect('lojinha_home')

@login_required(login_url='/login')
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    
    if request.method == 'POST':
        produto.nome = request.POST.get('nome')
        
        # Substitui a vírgula recebida do HTML por um ponto matemático
        preco_str = request.POST.get('preco', '0').replace(',', '.')
        produto.preco = float(preco_str)

        produto.tag = request.POST.get('tag')
        produto.save()
        return redirect('lojinha_home')
        
    return redirect('lojinha_home') # Redireciona caso o acesso não seja por POST

@login_required(login_url='/login')
def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    
    if request.method == 'POST':
        produto.delete()
        
    return redirect('lojinha_home')

def adicionar_carrinho(request, id):
    produto = get_object_or_404(Produto, id=id)
    
    # Recupera o carrinho da sessão atual ou cria um dicionário vazio se não existir
    carrinho = request.session.get('carrinho', {})
    
    # As chaves de dicionários em sessões (JSON) devem ser strings
    produto_id_str = str(produto.id)
    
    # Se o produto já existir no carrinho, apenas aumentamos a quantidade
    if produto_id_str in carrinho:
        carrinho[produto_id_str]['quantidade'] += 1
    else:
        # Se for um produto novo, registamos os dados básicos
        carrinho[produto_id_str] = {
            'nome': produto.nome,
            'preco': str(produto.preco),
            'quantidade': 1
        }
    
    # Guardamos o carrinho atualizado de volta na sessão do navegador
    request.session['carrinho'] = carrinho
    
    return redirect('lojinha_home')

def remover_carrinho(request, id):
    carrinho = request.session.get('carrinho', {})
    produto_id_str = str(id)
    
    # Remove do dicionário caso exista (evita erro 500 se o utilizador clicar duas vezes rápido)
    if produto_id_str in carrinho:
        del carrinho[produto_id_str]
        request.session['carrinho'] = carrinho
        
    return redirect('lojinha_home')