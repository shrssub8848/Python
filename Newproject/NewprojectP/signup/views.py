from django.shortcuts import render
from django.http import HttpResponse
from django import http


def signup(request):
    return render(request, 'home/signup.html')