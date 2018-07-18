from django import forms
from django.forms import TextInput
from .models import Link


class LinkForm(forms.Form):
    url = forms.URLField()
    url.widget.attrs.update({
        'placeholder': 'Enter Long URL',
        'autocomplete': 'off',
    })
