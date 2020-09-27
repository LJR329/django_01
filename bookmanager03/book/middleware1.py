from django.utils.deprecation import MiddlewareMixin


class Middleware(MiddlewareMixin):

    def process_request(self, request):
        print('每次请求调用')

    def process_response(self, request, response):
        print('每次响应调用')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('每次调用视图时调用！')
