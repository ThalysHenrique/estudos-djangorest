"""Estudos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.db import router
# importar o 'include'
from django.urls import path, include

# importar include e routers do rest_framework
# importar viewsets
from rest_framework import routers
from Paginas.api import viewsets as Paginasviewsets

# importar url de imagens

from django.conf.urls.static import static
from django.conf import settings

route = routers.DefaultRouter()
route.register(r'Paginas', Paginasviewsets.PaginasViewSet, basename = 'Paginas')

urlpatterns = [
    path('admin/', admin.site.urls),
    # importa as urls do app "Paginas"
    # consigo usar o "Paginas.urls" porque tem o __init__ e ele reconhece o "Paginas" como um pacote
    # deixando o primeiro parâmetro em branco consigo acessar diretamente do nome da url que indiquei dentro do urls "Paginas"
    path('', include(route.urls)),
    # incluir para imagens no final
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
