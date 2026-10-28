import urllib.parse

def carrinho_context(request):
    carrinho = request.session.get('carrinho', {})
    
    # Formata o preço de cada item individualmente
    for item in carrinho.values():
        item['preco_formatado'] = f"{float(item['preco']):.2f}".replace('.', ',')
        
    quantidade_total = sum(item['quantidade'] for item in carrinho.values())
    total_valor = sum(float(item['preco']) * item['quantidade'] for item in carrinho.values())
    total_formatado = f"{total_valor:.2f}".replace('.', ',')
    
    # Montagem da mensagem do WhatsApp
    link_whatsapp = "#"
    if carrinho:
        texto = "Olá! Gostaria de fazer o seguinte pedido:\n\n"
        for item in carrinho.values():
            texto += f"▪️ {item['quantidade']}x {item['nome']} (R$ {item['preco_formatado']})\n"
        texto += f"\n*Total: R$ {total_formatado}*"
        
        # Coloque o número do lojista (55 = Brasil, 85 = DDD do Ceará)
        numero_whatsapp = "5585992049066" 
        link_whatsapp = f"https://wa.me/{numero_whatsapp}?text={urllib.parse.quote(texto)}"
    
    return {
        'quantidade_carrinho': quantidade_total,
        'total_carrinho': total_formatado,
        'link_whatsapp': link_whatsapp
    }