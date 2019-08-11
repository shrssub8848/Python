from django.shortcuts import render
from django.http import HttpResponse
from django import http
from .import forms


def signup(request):
    form = forms.FormName(request.POST)
    if request.method == "POST":
        form = forms.FormName(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'home/signup.html', {'signup':form})
