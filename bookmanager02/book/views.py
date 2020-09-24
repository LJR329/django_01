from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from book.models import BookInfo


def creat(request):
    book = BookInfo.objects.create(
        name='create',

    )
    return HttpResponse('ok')