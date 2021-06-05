from django.forms import ModelForm
from django import forms
from .models import Type


class TypeForm(ModelForm):
    class Meta:
        model = Type
        fields = ['sortCd', 'name', 'color']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sortCd'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['color'].widget = forms.TextInput(attrs={'type':'color'})
        self.fields['color'].widget.attrs.update({'class': 'form-control'})