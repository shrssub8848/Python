from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django import http
from .import forms

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SignupSerializer
from .models import signup
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

def random(request):
    data = {1:{'name':'john','age':21},2:{'name':'jacky','age':28},3:{'name':'Hitoshi','age':31}}
    return JsonResponse(data)