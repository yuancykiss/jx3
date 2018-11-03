from django.conf.urls import url

# from qiyu.views import index
from qiyu import views

urlpatterns = [
    # 欢迎界面
    url(r'^index/', views.index, name='index'),
]