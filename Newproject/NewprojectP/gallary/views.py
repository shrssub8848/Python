from django.shortcuts import render
from django.http import HttpResponse
from django import http


def gallary(request):
    return render(request, 'home/gallary.html')