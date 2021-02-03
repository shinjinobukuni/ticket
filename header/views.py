from django.views import generic

class ListView(generic.TemplateView):
    template_name = "list.html"
