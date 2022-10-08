# preciso importar serializers da biblioteca rest_framework e o models do próprio diretório
from rest_framework import serializers
from Paginas import models

# classe serializer tem uma classe interna que se chama 'Meta' e recebe 2 parâmetros
class PaginasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Books
        # campos desse serializer 'fields' = está recebendo todos os campos do model
        # posso setar quais parâmetros quero que ele recebe > exemplo: ('id_book', 'state', 'upload_image_book')
        fields = '__all__'