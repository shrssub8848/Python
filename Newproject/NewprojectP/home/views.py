from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    dict = {'template_var':'This is jinja Var'}
    return render(request, 'index.html', context=dict)
