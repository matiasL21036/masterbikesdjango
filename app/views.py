from django.shortcuts import render
from .models import producto,arrendar
from .forms import ArrendarForm,ProductoForm
# Create your views here.

def home(request):
    productos = producto.objects.all()
    data = { 
        'productos': productos 
    }
    return render(request, 'app/home.html', data)


def arrendar(request):
    data = {
        'form': ArrendarForm()
    }

    if request.method == 'POST':
        formulario = ArrendarForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "ARRIENDO SOLICITADO, ESPERAR RESPUESTA VIA CORREO ELECTRONICO"
        else:
            data['form'] = formulario

    return render(request, 'app/arrendar.html', data)

def agregarprod(request):
    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,files=request.POST)
        if formulario.is_valid():
            formulario.save
            data["mensaje"]= "Producto publicado"
        else:
            data['form']= formulario


    return render(request, 'app/producto/agregar.html', data)


