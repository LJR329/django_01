from django.shortcuts import render, redirect
from django.http import HttpResponse


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


def redirect1(request):
    return redirect('http://www.baidu.com')


def set_cookie(request):
    username = request.GET.get('username')
    resp = HttpResponse('ok')
    resp.set_cookie('name', username)
    # resp.delete_cookie('name')  # 删除
    return resp


def get_cookie(request):
    name = request.COOKIES.get('name')
    return HttpResponse(name)


def set_session(request):
    name = request.GET.get('name')
    request.session['name'] = name

    return HttpResponse('ok')

def get_session(request):
    name = request.session.get('name')
    return HttpResponse(f'{name}')
