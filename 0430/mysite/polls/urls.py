from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^search_form/$', views.search_form, name='search_form'),
    url(r'^search/$', views.search, name="search"),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
]