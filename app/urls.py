from django.urls import path
from .views import home,arrendar, agregarprod



urlpatterns = [
    path('', home, name="home"),
    path('arrendar/', arrendar, name="arrendar"),
    path('agregarprod/',agregarprod,name="agregarprod")
    
]
