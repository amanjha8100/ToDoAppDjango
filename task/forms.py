from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'type':'text', 'placeholder':'Username', 'id':'username', 'name':'username', 'class' : 'form-control'})
        self.fields['email'].widget = forms.EmailInput(attrs={'type':'email','placeholder':'Email','id':'email','name':'email','class':'form-control'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'type':'password', 'placeholder':'Password....', 'id':'password1', 'name':'password1', 'class' : 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'type':'password', 'placeholder':'Confirm Password.....', 'id':'password2', 'name':'password2', 'class' : 'form-control'})
        

class AddForm(forms.Form):
    title = forms.CharField(max_length=120)
    msg = forms.CharField(widget=forms.Textarea)

class EditForm(forms.Form):
    title = forms.CharField(max_length=120)
    msg = forms.CharField(widget=forms.Textarea)
    status = forms.BooleanField(initial=False,required=False)