from django.views import generic
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.http import QueryDict
from .form import HeaderForm, HeaderUpdateForm
from .models import Header, Detail
from manageType.models import Type
import json
from django.utils import timezone

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
    form_class = HeaderUpdateForm
    model = Header

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #model = Header.objects.get(pk=context['pk'])

        return context


    def form_valid(self, form):
        messages.success(self.request, '更新しました。')

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '更新に失敗しました。')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('header:update', kwargs = {'pk': self.kwargs['pk']})

def getDetailList(request, headerId):

    details = Detail.objects.filter(header_id = headerId)
    jsonDetails = serializers.serialize('json', details)

    return HttpResponse(jsonDetails, content_type="text/json-comment-filtered")

def updateComment(request):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    addContent = body['addContent']
    headerId = body['headerId']
    status = body['status']

    header = Header.objects.get(pk = headerId)
    header.status = status
    header.save()

    detail = Detail(header_id = header, content = addContent, create_at = timezone.now())
    detail.save()

    details = Detail.objects.filter(header_id=headerId)
    jsonDetails = serializers.serialize('json', details)

    return HttpResponse(jsonDetails, content_type="text/json-comment-filtered")
# 忘備
# 参考リスト
# https://docs.djangoproject.com/ja/3.2/ref/csrf/
# https://qiita.com/kakimochi/items/4e95c9e4d1e4b00ec05a


