from django.shortcuts import render
from .models import Producto
from .models import Producto2
from .models import Producto3

# Create your views here.

def Main(request):
    productos = Producto3.objects.all()

    context = {
        'productos': productos
    }

    return render(request, 'autosdelmar/Main.html', context)


def hyundai(request):
    productos = Producto.objects.all()

    context = {
        "productos": productos
    }

    return render(request, 'autosdelmar/hyundai.html', context)


def compra(request):
    context={}
    return render(request, 'autosdelmar/compra.html', context)


def chevrolet(request):
    productos = Producto2.objects.all()

    context = {
        "productos": productos
    }

    return render(request, 'autosdelmar/chevrolet.html', context)


def About(request):
    context={}
    return render(request, 'autosdelmar/About.html', context)
