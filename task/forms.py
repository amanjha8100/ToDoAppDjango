from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        

class AddForm(forms.Form):
    title = forms.CharField(max_length=120)
    msg = forms.CharField(widget=forms.Textarea)

class EditForm(forms.Form):
    title = forms.CharField(max_length=120)
    msg = forms.CharField(widget=forms.Textarea)
    status = forms.BooleanField(initial=False,required=False)