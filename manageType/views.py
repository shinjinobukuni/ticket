from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Type
from .form import TypeForm


# Create your views here.
class ListView(generic.ListView):
    template_name = "manageType/list.html"
    model = Type

    def get_queryset(self):
        types = Type.objects.order_by('sortCd')
        return types

class TypeCreateView(generic.edit.CreateView):
    template_name = "manageType/create.html"
    model = Type
    form_class = TypeForm

    success_url = reverse_lazy('manageType:list')
