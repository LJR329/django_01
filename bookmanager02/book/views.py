from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.
from book.models import BookInfo


# url 路径参数
def index(request, cat_id, goods_id):
    print()
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
    print(request.META)
    return HttpResponse('ok')


def method(request):
    print(request.method)
    return HttpResponse('OK')


def response(request):
    # 1xx
    # 2xx  200成功
    # 3xx  重定向
    # 4xx  请求有问题　404路由有问题　　403权限问题
    # 5xx  服务器错误
    # return HttpResponse('ok', status=200)
    # info = {
    #     "name": "itcast",
    #     "addr": "changsha",
    # }
    info = [
        {
            "name": "itcast",
            "addr": "changsha",
        }
    ]
    # safe=true 表示data为字典数据
    return JsonResponse(data=info, safe=False)
    # return redirect("http://www.baidu.com")  # 重定向
