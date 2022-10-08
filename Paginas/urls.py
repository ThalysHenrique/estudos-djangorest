# import path / IndexView at views.py
# O . significa que estou importando algo de dentro do diretório, no caso "Paginas"
# Quando começa com "django" está pegando do módulo "pip install django"
# urls está dentro do django
# usa apenas o .views pq se fosse .views.py, o django irá achar que tem py dentro de views
from ast import Index
from django.urls import path
from .views import IndexView

urlpatterns = [
    # dentro de path usa 3 parâmetros (o que o usuário vai digitar para acessar, qual vai ser a view que vai ser chamada, nome)
    # path ('Endereço', MinhaView.as_view(), name='name_of_url'),
    path ('home/', IndexView.as_view(), name='Home'),
]