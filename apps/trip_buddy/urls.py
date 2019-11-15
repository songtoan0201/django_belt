from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^dashboard$', views.dashboard),
    url(r'^trips/(?P<number>\d+)$', views.show),
    url(r'^trips/edit/(?P<number>\d+)$', views.edit),
    url(r'^trips/new$', views.add),
    url(r'^trips/destroy/(?P<number>\d+)$', views.delete),
    url(r'^trips/join/(?P<trip_id>\d+)$', views.join),
    url(r'^trips/cancel/(?P<trip_id>\d+)$', views.cancel),

]
