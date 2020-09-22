from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


"""
所谓的视图就是python函数
视图函数有两个要求：
    1. 视图函数的第一个参数就是接受请求  这个请求就是HttpRequest类的对象
    2. 必须返回一个响应
"""

# /index-
def index(request):
    return HttpResponse('OK')
