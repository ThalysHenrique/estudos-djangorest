from distutils.command.upload import upload
from email.policy import default
from uuid import uuid4
from django.db import models
from uuid import uuid4

# função de upload de imagem para armazenar nome do arquivo que queremos guardar
# recebe uma instancia do (classe)objeto book
def upload_image_book(instance, filename):
    # esta recebendo id da instancia do objeto book
    # em seguido o nome do arquivo para não ter riscos de ter dois arquivos com o mesmo nome
    return f"{instance.id_book}-{filename}"

class Books(models.Model):
    id_book = models.UUIDField(primary_key = True, default = uuid4, editable = False)
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    release_year = models.IntegerField()
    state = models.CharField(max_length = 255)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length = 255)
    create_at = models.DateField(auto_now_add = True)
    # upload_to recebe a função
    # true = pode ficar em branco ou nulo // false = obrigatório
    image = models.ImageField(upload_to=upload_image_book, blank = True, null = True)


    def __str__(self):
        return self.title
    