from django.forms import ModelForm, Textarea, TextInput, FileInput, NumberInput, CheckboxInput
from .models import Advertisements
from django import forms


def dont_question_mark(value):
    if value.lower().startswith(u'?'):
        msg = u'Заголовок не может начинаться с вопросительного знака'
        raise ValueError(msg)


class AdvertisementsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdvertisementsForm, self).__init__(*args, **kwargs)
        self.fields['title'].validators = [dont_question_mark]
        self.fields['image'].required = False
        self.fields['auction'].required = False

    class Meta:
        model = Advertisements
        fields = ['title', 'description', 'image', 'price', 'auction']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': Textarea(attrs={'class': 'form-control form-control-lg'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'price': NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'auction': CheckboxInput(attrs={'class': 'form-check-input'})
        }

