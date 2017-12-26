from django.conf.urls import url

from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.landing, name='index'),
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^index/$', views.indexSipun, name="indexSipun"),
    url(r'^signup/$', views.signupSipun, name="signupSipun"),
    url(r'^orderForm/$', views.orderFormSipun, name="orderFormSipun"),
    url(r'^register/$', views.registerSipun, name="registerSipun"),
]
