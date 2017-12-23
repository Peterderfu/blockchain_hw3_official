from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^config', views.getConfig),
    url(r'^history', views.getHistory),
    url(r'^symbols', views.getSymbols),
]