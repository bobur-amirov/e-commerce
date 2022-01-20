from django import forms

from .models import UserBase


class UserBaseRegisterForm(forms.ModelForm):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=15, help_text='Required')
    email = forms.EmailField(label='Enter Email', max_length=50, help_text='Required',
                             error_messages={'required': 'Sorry!'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ['email', 'username']

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        user = UserBase.objects.filter(username=username)
        if user.count():
            raise forms.ValidationError("Username already exists")
        return username

    def clean_password2(self):
        pas = self.cleaned_data
        if pas['password'] != pas['password2']:
            raise forms.ValidationError("Password do not match! ")
        return pas['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError('Please use another Email, that is already token')
        return email

