from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def sample(request):
    return HttpResponse("Hello, World!")
