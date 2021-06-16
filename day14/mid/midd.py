from django.utils.deprecation import MiddlewareMixin


# class CustomHeaderMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         request.META['HTTP_CUSTOM_HEADER'] = "wrold"

class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['hello'] = "world"
        return response