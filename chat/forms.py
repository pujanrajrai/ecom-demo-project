from django import forms
from .models import Chat


class ChatForms(forms.ModelForm):
    message = forms.CharField(max_length=500, min_length=1, required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = Chat
        fields = [
            'message',
            'image'
        ]
