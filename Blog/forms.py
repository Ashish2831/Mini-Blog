from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from .models import *

class Register_Form(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class' : 'form-control'}), required=False)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class' : 'form-control'}), required=False)
    
    def __init__(self, *args, **kwargs):
        super(Register_Form, self).__init__(*args, **kwargs)
        self.label_suffix = ''
        self.fields.get('username').required = False
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

        labels = {
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'email' : 'Email',
        }

        help_texts = {
            'username' : ''
        }

        widgets = {
            'first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'username' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
        }

    def clean_username(self):
        inp_username = self.cleaned_data.get('username')
        if len(inp_username.strip()) == 0:
            raise ValidationError(_("Please Enter The Username!!"))
        return inp_username

    def clean_first_name(self):
        inp_first_name = self.cleaned_data.get('first_name')
        if len(inp_first_name.strip()) == 0:
            raise ValidationError(_("Please Enter Your First Name!!"))
        return inp_first_name

    def clean_last_name(self):
        inp_last_name = self.cleaned_data.get('last_name')
        if len(inp_last_name.strip()) == 0:
            raise ValidationError(_("Please Enter Your Last Name!!"))
        return inp_last_name

    def clean_email(self):
        inp_email = self.cleaned_data.get('email')
        validator = EmailValidator(_("Please Provide Valid Email!!"))
        validator(inp_email)
        return inp_email

    def clean_password1(self):
        inp_password1 = self.cleaned_data.get('password1')
        if len(inp_password1) == 0:
            raise ValidationError(_("Please Enter The Password!!"))
        return inp_password1

    def clean_password2(self):
        inp_password2 = self.cleaned_data.get('password2')
        inp_password1 = self.data.get('password1')
        if len(inp_password2) == 0:
            raise ValidationError(_("Please Confirm Your Password!!"))
        if inp_password1 != inp_password2:
            raise ValidationError(_("Password Must Matched!!"))
        return inp_password2

class Post_Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control'})
        }