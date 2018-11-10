from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
# import os, django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'jx3.settings')# project_name 项目名称
# django.setup()
#
# def index(request):
#     if request.method == 'GET':
#         return render(request, 'experience.html')
from rest_framework.views import APIView

from experience.models import Experience


# class APIView(View):
#     pass


class ExperienceView(APIView):

    # def dispatch(self, request, *args, **kwargs):
    #     func = getattr(self, request.method)
    #     return func(self, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        list = Experience.objects.all()
        return render(request, 'experience.html', {"list": list})

    def post(self, request, *args, **kwargs):
        data = request.POST
        expreience = Experience.objects.all().first()
        print(expreience)
        return HttpResponse('this is POST')