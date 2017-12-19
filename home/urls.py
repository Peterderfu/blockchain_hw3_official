from django.conf.urls import url

from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.landing, name='index'),
    url(r'^price-realtime', views.priceRealtime, name="priceRealtime"),
    url(r'^index', views.indexSipun, name="indexSipun"),
    url(r'^index.html', views.indexSipun, name="indexSipun"),
    url(r'^signup', views.signupSipun, name="signupSipun"),
    url(r'^orderForm', views.orderFormSipun, name="orderFormSipun"),
    url(r'^register', views.registerSipun, name="registerSipun"),
]
