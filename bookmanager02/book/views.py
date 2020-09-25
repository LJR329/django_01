from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.
from book.models import BookInfo


# url 路径参数
def index(request, cat_id, goods_id):
    return JsonResponse({'cat_id': cat_id, 'id': goods_id})


# 查询字符串
# def string(request):
#     print(request.GET)
#     return HttpResponse('ok')
#

# 查询字符串  一键多值
def string(request):
    query = request.GET
    print(query)
    print(query.get('kw'))
    print(query.getlist('kw'))
    return HttpResponse('ok')


def register(request):
    return HttpResponse('ok')


def json1(request):
    body = request.body.decode()
    print(json.loads(body))
    return HttpResponse('ok')
