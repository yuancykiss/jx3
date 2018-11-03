from django.conf.urls import url

from experience import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),

]