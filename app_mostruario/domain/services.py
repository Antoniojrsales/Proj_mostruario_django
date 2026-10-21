from django.db import models

class Produto(models.Model):
    # Opções para o select da Tag de Destaque
    TAG_CHOICES = [
        ('normal', 'Normal'),
        ('mais_vendidos', 'Mais vendidos'),
        ('promocao', 'Promoção'),
    ]

    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    tag = models.CharField(max_length=20, choices=TAG_CHOICES, default='normal')
    # O upload_to define a pasta onde as imagens serão guardadas (dentro da pasta media)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    
    # Campo de controlo de data de criação
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome