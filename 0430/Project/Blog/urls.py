from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^Mothers_Day/$', views.Mothers_Day, name='Mothers_Day'),
    url(r'^blog/$', views.blog, name='blog'),
]