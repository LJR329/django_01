from django.urls import path
from book import views
from django.urls.converters import register_converter


class MobileConverter:
    """自定义路由转换器：匹配手机号"""
    # 匹配手机号码的正则
    regex = '1[3-9]\d{9}'

    def to_python(self, value):
        # 将匹配结果传递到视图内部时使用
        return int(value)

    def to_url(self, value):
        # 将匹配结果用于反向解析传值时使用
        return str(value)


register_converter(MobileConverter, 'phone')    # 注册才能使用

urlpatterns = [
    path('<int:cat_id>/<phone:goods_id>', views.index),
    path('string/', views.string),
    path('register/', views.register),
    path('json/', views.json1),
    path('method/', views.method),
    path('res/', views.response)
]
