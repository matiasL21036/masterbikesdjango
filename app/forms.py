from django import forms
from .models import arrendar,producto

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