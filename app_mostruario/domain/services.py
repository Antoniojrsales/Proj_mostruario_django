from django.db import models
from PIL import Image

class Produto(models.Model):
    # Opções para o select da Tag de Destaque
    TAG_CHOICES = [
        ('destaque_semana', 'Destaque Semana'),
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

    def save(self, *args, **kwargs):
        # 1. Salva o produto original no banco de dados primeiro
        super().save(*args, **kwargs)

        # 2. Se houver uma imagem no upload, abre o ficheiro físico
        if self.imagem:
            img = Image.open(self.imagem.path)

            # 3. Se a imagem for maior que 800x800 pixels, redimensiona
            if img.height > 800 or img.width > 800:
                tamanho_maximo = (800, 800)
                img.thumbnail(tamanho_maximo)
                
                # 4. Sobrescreve a imagem aplicando compressão e cortando o "peso"
                img.save(self.imagem.path, quality=70, optimize=True)