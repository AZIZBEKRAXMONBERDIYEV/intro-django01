from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
import requests


URL = 'https://randomuser.me/api/?results=30'


def users(request: HttpRequest):
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()

        users = data['results']
        return JsonResponse(users, safe=False)

    return JsonResponse({'error': 'Something went wrong'})

