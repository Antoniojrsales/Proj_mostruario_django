from django.urls import path
from . import views

urlpatterns = [
    path('', views.lojinha_home, name='lojinha_home'),
    path('login/', views.login_lojista, name='login_lojista'),
    path('produto/novo/', views.cadastrar_produto, name='cadastrar_produto'),
]