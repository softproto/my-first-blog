from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the blog/index/ index.")


def post_list(request):
    return render(request, 'blog/post_list.html', {})
