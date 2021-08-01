from django import forms
from .models import Header
from manageType.models import Type
from django.contrib.admin.widgets import AdminDateWidget
import bootstrap_datepicker_plus as datetimepicker

class TypeChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj): # label_from_instance 関数をオーバーライド
        return str(obj.sortCd) + " : " +obj.name

class HeaderForm(forms.ModelForm):

    type_cls = TypeChoiceField(queryset=Type.objects.all().order_by('sortCd'), label='種別', required=False)

    class Meta:
        model = Header
        fields = ['type_cls', 'title', 'content','limit_date', 'status']



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type_cls'].widget.attrs.update({'class': 'form-control col-lg-3'})
        self.fields['title'].widget.attrs.update({'class': 'form-control col-lg-10'})
        self.fields['content'].widget = forms.Textarea(attrs={'rows':8, 'cols':15})
        self.fields['content'].widget.attrs.update({'class': 'form-control col-lg-10'})
        self.fields['limit_date'].widget = datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            )
        self.fields['limit_date'].widget.attrs.update({'class': 'form-control col-lg-2'})
        self.fields['status'].widget.attrs.update({'class': 'form-control col-lg-3'})

class HeaderUpdateForm(forms.ModelForm):

    type_cls = TypeChoiceField(queryset=Type.objects.all().order_by('sortCd'), label='種別', required=False)

    class Meta:
        model = Header
        fields = ['type_cls', 'title', 'content']



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type_cls'].widget.attrs.update({'class': 'form-control col-lg-3'})
        self.fields['title'].widget.attrs.update({'class': 'form-control col-lg-10'})
        self.fields['content'].widget = forms.Textarea(attrs={'rows':8, 'cols':15})
        self.fields['content'].widget.attrs.update({'class': 'form-control col-lg-10'})
