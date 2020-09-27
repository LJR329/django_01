from django.utils.deprecation import MiddlewareMixin


class TestMiddleWare(MiddlewareMixin):

    # 每次请求调用
    def process_request(self, request):
        print('每次请求都会执行')
        usernma = request.GET.get('username')
        if usernma is None:
            print('没有用户信息!')
        else:
            print('有用户信息!')

    # 每次响应前多会执行
    def process_response(self, request, response):
        print('每次响应前都会执行')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # 处理视图前自动调用
        print('process_view1 被调用')
