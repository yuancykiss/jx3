from django.core.cache import caches
from django.http import JsonResponse


def my_middleware(message_code):
    def middle(request):
        if request.path.startswith('/index/code'):
            phone = request.GET.get('phone')
            if caches['code'].get(phone):
                data = {
                    'code': 401,
                    'message': '请在６０ｓ后重试'
                }
                return JsonResponse(data)
            return message_code(request)
    return middle