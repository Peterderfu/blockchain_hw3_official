from django.conf.urls import url

from . import views

app_name = 'wallet'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'bitcoin^$', views.bitcoin, name='bitcoin'),
    # url(r'ethereum^$', views.ethereum, name='ethereum'),
    # url(r'iota^$', views.iota, name='iota'),
]
