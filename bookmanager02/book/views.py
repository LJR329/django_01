from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from book.models import BookInfo

# url 路径参数
def index(request, cat_id, goods_id):
    return JsonResponse({'cat_id': cat_id, 'id': goods_id})

# 查询字符串
def string(request):
    

    return