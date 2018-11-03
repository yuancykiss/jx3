from django.conf.urls import url

from qiyu.views import index

urlpatterns = [
    # 欢迎界面
    url(r'^admin/', index, name='index'),
]