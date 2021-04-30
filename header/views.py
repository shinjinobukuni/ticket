from django.views import generic

from .models import Header

class ListView(generic.ListView):
    template_name = "header/list.html"
    model = Header

    def get_queryset(self):
        headers = Header.objects.order_by('id')
        return headers
