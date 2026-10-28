from django.urls import path
from . import views

urlpatterns = [
    path('', views.lojinha_home, name='lojinha_home'),
    path('login/', views.login_lojista, name='login_lojista'),
    path('produto/novo/', views.cadastrar_produto, name='cadastrar_produto'),
    path('logout/', views.logout_lojista, name='logout_lojista'),
    path('produto/<int:id>/editar/', views.editar_produto, name='editar_produto'),
    path('produto/<int:id>/excluir/', views.excluir_produto, name='excluir_produto'),
    path('carrinho/<int:id>/adicionar-carrinho/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('produto/<int:id>/remover-carrinho/', views.remover_carrinho, name='remover_carrinho'),
]