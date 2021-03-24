from django import forms
from .models import MyUser


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(min_length=3, max_length=70)
    username = forms.CharField(min_length=5, max_length=70)
    date_of_birth = forms.DateField()
    password = forms.CharField(min_length=7, max_length=70, widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=7, max_length=70, widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ['email', 'username', 'date_of_birth', 'password', 'password2']

    # password validation
    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('passwords fields did not match')

