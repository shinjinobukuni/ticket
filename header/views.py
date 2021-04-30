from django.views import generic
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .form import HeaderForm

from .models import Header

from manageType.models import Type

class ListView(generic.ListView):
    template_name = "header/list.html"
    model = Header

    def get_queryset(self):
        headers = Header.objects.order_by("type_cls__sortCd")
        return headers

class HeaderCreateView(CreateView):
    template_name = "header/create.html"
    model = Header
    form_class = HeaderForm

    success_url = reverse_lazy('header:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type_list'] = Type.objects.all().order_by('sortCd')
        return context

