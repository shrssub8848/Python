from django.shortcuts import render
from django.http import HttpResponse
from django import http


def about(request):
    return render(request, 'home/about.html')