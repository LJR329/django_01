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


# def response(request):
#     # 1xx
#     # 2xx  200成功
#     # 3xx  重定向
#     # 4xx  请求有问题　404路由有问题　　403权限问题
#     # 5xx  服务器错误
#     # return HttpResponse('ok', status=200)
#     # info = {
#     #     "name": "itcast",
#     #     "addr": "changsha",
#     # }
#     info = [
#         {
#             "name": "itcast",
#             "addr": "changsha",
#         }
#     ]
#     # safe=true 表示data为字典数据
#     return JsonResponse(data=info, safe=False)
#     # return redirect("http://www.baidu.com")  # 重定向


"""
第一次请求携带查询字符串
服务器接受到请求之后，获取信息，服务器设置cookie  保存cookie
第二次访问都会携带cookie信息
服务器通过cookie信息判断用户身份
"""


def set_cookie(request):
    username = request.GET.get('username')
    # 设置cookie  通过响应对象set_cookie
    response = HttpResponse('cookie')
    # 设置cookie
    response.set_cookie('name', username, max_age=360000)  # max_age 是一个秒数 cookie的时间
    # response.delete_cookie('name')  # 删除cookie
    return response


def get_cookie(request):
    # 获取cookie信息
    cookies = request.COOKIES.get('name')
    return HttpResponse(cookies)
