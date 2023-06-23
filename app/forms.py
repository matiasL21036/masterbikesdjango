from django import forms
from .models import arrendar,producto, OrdenReparacion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ArrendarForm(forms.ModelForm):

    class Meta:
        model = arrendar
        fields = '__all__'

       


class ProductoForm(forms.ModelForm):

    class Meta:
        model = producto
        fields = '__all__'
        widgets = {

            "fecha_fabricacion" : forms.SelectDateWidget()
        }

class OrdenReparacionForm(forms.ModelForm):
    
        class Meta:
            model = OrdenReparacion
            fields = [ "mecanico", "bicicleta_nombre", "descripcion_problema", "tipo" , "Usuario"]

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1",'password2']