from django.urls import path
from .views import home,arrendar, agregarprod,listarprod,modificar,eliminar



urlpatterns = [
    path('', home, name="home"),
    path('arrendar/', arrendar, name="arrendar"),
    path('agregarprod/',agregarprod,name="agregarprod"),
    path('listarprod/',listarprod,name="listarprod"),
    path('modificarprod/<id>/',modificar,name="modificar"),
    path('elimnarprod/<id>/',eliminar,name="eliminar")
    
]
