
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from experience.models import Experience


class ExperienceView(APIView):

    def get(self, request, *args, **kwargs):
        list1 = Experience.objects.all()
        paginator = Paginator(list1, 40)
        try:
            page = int(request._request.GET.get('page'))
        except:
            page = int(1)
        list = paginator.page(page)
        return render(request, 'experience.html', {"list": list})


    def post(self, request, *args, **kwargs):
        data = request.POST.get('aa')
        expreience = Experience.objects.all().first()
        print(expreience)
        return HttpResponse('this is POST')


class CountInfo(APIView):
    def get(self, request, *args, **kwargs):
        count_info = request.GET.get('info')
        print(count_info)
        result = Experience.objects.values(count_info).all().annotate(count=Count(count_info))
        results = [(item[count_info], item['count']) for item in result]
        return JsonResponse({'info': results})
