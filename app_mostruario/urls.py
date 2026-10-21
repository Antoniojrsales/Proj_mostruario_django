from django.urls import path
from . import views

app_name = 'mostruario'

urlpatterns = [
    path('', views.lojinha_home, name='lojinha_home'),
]