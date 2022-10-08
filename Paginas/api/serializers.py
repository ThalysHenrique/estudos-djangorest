# preciso importar serializers da biblioteca rest_framework e o models do próprio diretório
from rest_framework import serializers
from Paginas import models

# classe serializer tem uma classe interna que se chama 'Meta' e recebe 2 parâmetros
class PaginasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Books
        # campos desse serializer 'fields = todos os campos do model
        fields = '__all__'