from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

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

    def form_valid(self, form):
        messages.success(self.request, '追加しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '追加に失敗しました。')
        return super().form_invalid(form)


class TypeUpdateView(generic.edit.UpdateView):
    template_name = "manageType/update.html"
    model = Type
    form_class = TypeForm

    success_url = reverse_lazy('manageType:list')

    def form_valid(self, form):
        messages.success(self.request, '更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field in form:
            for error in field.errors:
                messages.error(self.request, error)

        return super().form_invalid(form)



class TypeDeleteView(generic.edit.DeleteView):
    model = Type
    success_url = reverse_lazy('manageType:list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, '削除しました。')
        return super().delete(request, *args, **kwargs)
