import time

from django.shortcuts import render
from rest_framework.views import APIView

from actor.models import Daqu, Server
from utils.qiyu import get_qiyu


class QiyuView(APIView):

    def get(self, request):
        daqus = Daqu.objects.all()
        servers = Server.objects.all()
        print(daqus.values('name'))
        print(servers.values('name'))
        return render(request, 'qiyu.html', {'daqus': daqus, 'servers': servers})

    def post(self, request):
        results = request.POST.get('sdf')
        # result = get_qiyu()
        result = []
        for item in result:
            st = time.localtime(int(item['time']))
            local_time = time.strftime('%Y-%m-%d %H:%M:%S', st)
            item['time'] = local_time
        print(result)
        # return render(request, 'qiyu.html', {'result': result})
