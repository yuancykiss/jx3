from django.conf.urls import url

from experience import views
from actor.views import IndexView

urlpatterns = [
    url('', IndexView.as_view()),
]