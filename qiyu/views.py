from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from utils.qiyu import get_qiyu


class QiyuView(APIView):

    def get(self, request,  *args, **kwargs):
        # result = get_qiyu()
        return render(request, 'qiyu.html')
