from django.urls import path
from .views import home,arrendar, agregarprod,listarprod,modificar,eliminar, login, registro, arreglar



urlpatterns = [
    path('', home, name="home"),
    path('arrendar/', arrendar, name="arrendar"),
    path('agregarprod/',agregarprod,name="agregarprod"),
    path('listarprod/',listarprod,name="listarprod"),
    path('modificarprod/<id>/',modificar,name="modificar"),
    path('elimnarprod/<id>/',eliminar,name="eliminar"),
    path('login',login,name='login'),
    path('registro',registro,name='registro'),
    path('arreglar',arreglar,name='arreglar'),
    
]
