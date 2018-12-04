from django.conf.urls import url

from experience import views

urlpatterns = [
    url(r'^index/', views.ExperienceView.as_view()),
    url(r'^count/', views.CountInfo.as_view()),
]