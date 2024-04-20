from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'onepiece/index.html')

def equipages(request):
    return render(request, 'onepiece/equipages.html')