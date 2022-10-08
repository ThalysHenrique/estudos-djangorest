from django.views.generic import TemplateView

# quando digitar a url "index.html" irá renderizar essa view
class IndexView(TemplateView):
    template_name = "index.html"