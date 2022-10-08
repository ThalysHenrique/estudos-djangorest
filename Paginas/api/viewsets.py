# preciso importar viewsets do pacote rest_framework e serializers do próprio diretório 'Paginas.api'
from rest_framework import viewsets
from Paginas.api import serializers
from Paginas import models

class PaginasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PaginasSerializer
    # queryset = todos os campos do nosso model
    queryset = models.Books.objects.all()