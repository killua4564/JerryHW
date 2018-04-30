from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^search_form/$', views.search_form, name='search_form'),
    url(r'^search/$', views.search, name="search"),
]