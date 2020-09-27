from django.utils.deprecation import MiddlewareMixin


class TestMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        print('每次请求都会执行')
        usernma = request.GET.get('username')
        if usernma is None:
            print('没有用户信息!')
        else:
            print('有用户信息!')

    def process_response(self, request, response):
        print('每次响应前都会执行')
        return response
