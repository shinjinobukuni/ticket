from django.views import generic
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .form import HeaderForm
from .models import Header
from manageType.models import Type

class ListView(generic.ListView):
    template_name = "header/list.html"
    model = Header
    paginate_by = 5

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

    def form_valid(self, form):
        messages.success(self.request, '追加しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '追加に失敗しました。')
        return super().form_invalid(form)

class HeaderUpdateView(generic.edit.UpdateView):
    template_name = "header/update.html"
    model = Header
    form_class = HeaderForm
