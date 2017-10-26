from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tos/$', views.tos, name='tos'),
    url(r'^order/$', views.order, name='order'),
]