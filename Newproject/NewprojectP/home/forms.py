from django import forms
from .models import signup

class FormName(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput)


    class Meta:
        model = signup
        fields = "__all__"