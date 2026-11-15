from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app_mostruario.api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_mostruario.urls')),   
    path('api/', api.urls),
    path('', include('django_prometheus.urls')),
]

# Adicionar o mapeamento da pasta media durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
