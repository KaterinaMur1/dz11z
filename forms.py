# from django import forms
# from django.core.exceptions import ValidationError

# def dont_question_mark(value):
#     if value[0] == '?':
#         msg = 'Заголовок не может начинаться с вопросительного знака'
#         raise ValidationError(msg)

# class AdvertisementForm(forms.Form):
#     title = forms.CharField(max_length=64, validators=[dont_question_mark], widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
#     image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}), required=False)
#     price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
#     auction = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)



from django.forms import ModelForm, Textarea, TextInput, FileInput, NumberInput, CheckboxInput
from .models import Advertisements
from django import forms


def dont_question_mark(value):
    if value.lower().startswith(u'?'):
        msg = u'Заголовок не может начинаться с вопросительного знака'
        raise ValueError(msg)

# def dont_question_mark(self):
#     title = self.cleaned_data['title']
#     if "?" in title:
#         raise ValidationError('Заголовок не может начинаться с вопросительного знака')
#     return title


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

