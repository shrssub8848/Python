from django.shortcuts import render
from django.http import HttpResponse
from django import http
from .import forms

# Create your views here.

def home(request):
    dict = {'template_var':'This is jinja Var'}
    return render(request, 'home/index.html', context=dict)


def signup(request):
    form = forms.FormName(request.POST)
    if request.method == "POST":
        form = forms.FormName(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'home/signup.html', {'signup:form'})
