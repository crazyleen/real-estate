from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^evaluate/$', views.evaluate, name='evaluate'),
    url(r'^relation/$', views.relation, name='relation'),
    url(r'^desire/$', views.desire, name='desire'),
]