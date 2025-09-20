from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def atracoes(request):
    return render(request, 'atracoes.html')

def historia(request):
    return render(request, 'historia.html')

def galeria(request):
    return render(request, 'galeria.html')
