from django.shortcuts import render

def lojinha_home(request):
    return render(request, 'app_mostruario/pages/lojinha.html')