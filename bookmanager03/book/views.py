from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.


def index(request):
    # user = request.GET.get('user')
    user = request.GET.getlist('user')
    return HttpResponse(f'{user}')


def goods(request, cat_id, goods_id):
    return HttpResponse(f"{cat_id}, {goods_id}")


def string(request):
    get = request.GET
    print(get)
    return HttpResponse(f'ok')


def post(request):
    print(request.POST)
    return HttpResponse('ok')


def header(request):
    print(request.META)
    print(request.method)
    print(request.user)
    return HttpResponse('ok')
