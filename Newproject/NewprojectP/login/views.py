from django.shortcuts import render
from django.http import HttpResponse
from django import http


def login(request):
    return render(request, 'home/login.html')