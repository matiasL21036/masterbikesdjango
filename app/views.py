from django.shortcuts import render,redirect,get_object_or_404
from .models import producto,arrendar
from .forms import ArrendarForm,ProductoForm, OrdenReparacionForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
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
        formulario = ProductoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Producto publicado"
        else:
            data['form'] = formulario

    return render(request, 'app/producto/agregar.html', data)



def listarprod(request):
    productos = producto.objects.all()
    
    data = { 
        'productos': productos 
    
    }

    return render(request,'app/producto/listar.html',data)

def modificar(request, id):
    producto_obj = get_object_or_404(producto, id=id)
    data = {
        'form': ProductoForm(instance=producto_obj)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto_obj, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarprod")
        data['form'] = formulario

    return render(request, 'app/producto/modificar.html', data)

def eliminar(request, id):
    producto_obj = get_object_or_404(producto, id=id)
    producto_obj.delete()
    return redirect('listarprod')

def login(request):
    return render(request, 'registration/login.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Usuario creado")
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/register.html' , data)

def arreglar(request):
    data = {
        "form": OrdenReparacionForm()
    }
    if request.method == 'POST':
        formulario = OrdenReparacionForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Orden de reparacion creada")
        else:
            messages.error(request, "Error al crear orden de reparacion" )
            data['form'] = formulario
    return render(request, 'app/user/arreglar.html', data)


def modificarUser(request, username):
    user = get_object_or_404(User, username=username)
    data = {
        'form': CustomUserCreationForm(instance=user)
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST, instance=user)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="home")
        data['form'] = formulario
    return render(request, 'registration/modificar.html', data)
