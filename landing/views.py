from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     return HttpResponse("Hello, world. You're at the landing index.")

def home(request):
    return render(request, 'landing/home.html', {})
