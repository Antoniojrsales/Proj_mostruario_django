from ninja import NinjaAPI, ModelSchema
from .models import Produto
from typing import List

# Inicializa a API com título para a documentação Swagger
api = NinjaAPI(title="API Mostruário - Plataforma Barra", version="1.0.0")

# Define o Schema serializador baseado no seu Model existente
class ProdutoSchema(ModelSchema):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco', 'tag'] 

# Cria o endpoint GET /api/produtos/
@api.get("/produtos/", response=List[ProdutoSchema], summary="Lista todos os produtos")
def listar_produtos(request):
    return Produto.objects.all()