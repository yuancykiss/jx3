from django.conf.urls import url

from actor import views
from actor.views import IndexView

urlpatterns = [
    url('index', IndexView.as_view()),
    url(r'code/', views.message_code, name='code')
]