from django.conf.urls import url
from . import views
from .models import Relay

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'GRB200|GBU200|GRL200|GRZ200|GRD200/',views.detail,name='detail')
]
