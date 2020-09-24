from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from book.models import BookInfo


def creat(request):
    a = request.GET
    print(a)
    return HttpResponse('ok')