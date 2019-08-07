from django.shortcuts import render
from django.http import HttpResponse
from django import http

# Create your views here.

def home(request):
    dict = {'template_var':'This is jinja Var'}
    return render(request, 'home/index.html', context=dict)


