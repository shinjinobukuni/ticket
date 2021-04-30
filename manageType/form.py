from django.forms import ModelForm
from .models import Type


class TypeForm(ModelForm):
    class Meta:
        model = Type
        fields = ['sortCd', 'name', 'color']
        # widgets = {
        #     'limit_date' : AdminDateWidget()
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sortCd'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        # self.fields['color'].widget.attrs.update({'class': 'form-control col-lg-2'})