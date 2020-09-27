from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.views import View


# 获取url路径参数
def index(request):
    # user = request.GET.get('user')
    # request.GET.get('name')
    user = request.GET.getlist('user')
    return HttpResponse(f'{user}')


# 获取商品编号
def goods(request, cat_id, goods_id):
    return HttpResponse(f"{cat_id}, {goods_id}")


# 获取url路径信息
def string(request):
    get = request.GET
    print(get)
    return HttpResponse(f'ok')


# 获取表单提交参数
def post(request):
    print(request.POST)
    return HttpResponse('ok')


def header(request):
    # 获取请求头数据
    print(request.META)
    # 获取请求方式
    print(request.method)
    # 获取请求用户对象
    print(request.user)
    return HttpResponse('ok')


# 重定向
def redirect1(request):
    return redirect('http://www.baidu.com')


# 设置cookie
def set_cookie(request):
    username = request.GET.get('username')
    resp = HttpResponse('ok')
    resp.set_cookie('name', username)
    # resp.delete_cookie('name')  # 删除
    return resp


# 获取cookie
def get_cookie(request):
    name = request.COOKIES.get('name')
    return HttpResponse(name)


# 设置session
def set_session(request):
    name = request.GET.get('name')
    request.session['name'] = name

    return HttpResponse('ok')


# 获取session
def get_session(request):
    name = request.session.get('name')
    return HttpResponse(f'{name}')


# 定义类视图
class LoginView(View):
    def post(self, request):
        return HttpResponse('post')

    def get(self, request):
        return HttpResponse('get')


################################################################

"""

我的订单，个人中心页面
如果登录用户 可以访问
如果未登录用户  不应该访问  应该跳转到登录页面
定义一个订单， 个人中心， 类视图


"""
# from django.contrib.auth.mixins import LoginRequiredMixin
#
#
# # LoginRequiredMixin 内部会进行用户是否登录判断 如果没有登录会跳转到accounts页面
# class OrderView(LoginRequiredMixin, View):
#
#     def get(self, request):
#         # isLogin = False
#         # if not isLogin:
#         #     return HttpResponse('你没有登录。。。跳转到登录页面中')
#         return HttpResponse('get')
#
#     def post(self, request):
#         return HttpResponse('post')
from django.contrib.auth.mixins import LoginRequiredMixin


# from django.contrib.auth.mixins import LoginRequiredMixin

class OrderView(LoginRequiredMixin, View):
    def get(self, request):
        return HttpResponse('get')

    def post(self, request):
        return HttpResponse('post')
