from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
import json

def home(request):
    return HttpResponse("Hello, Django!")

def about(request):
    return HttpResponse("This is an about page!")

def get_data(request):
    data = {
        "name": "John",
        "age": 30
    }
    return JsonResponse(data)