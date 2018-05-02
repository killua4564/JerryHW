from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.blog, name='blog'),
    url(r'^new/', views.new, name="new"),
    url(r'^edit/', views.edit, name="edit"),
]