from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'child'

urlpatterns=[
    url(r"^addinfo/$", views.HelperView, name='helper'),
    url(r"^searchinfo/$", views.PoliceView, name='police'),
    url(r"^result/$", views.ResultView, name='result'),
]
