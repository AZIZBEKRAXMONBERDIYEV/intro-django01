from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import json

def home(request):
    return HttpResponse("Hello, Django!")

def about(request):
    return HttpResponse("This is an about page!")