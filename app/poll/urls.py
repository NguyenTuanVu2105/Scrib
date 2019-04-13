from django.conf.urls import url

from . import views

app_name = "poll"
urlpatterns = [
    url(r"(\d+)/", views.poll, name="detail"),
    url(r"^show/", views.show, name="unvoted"),
    url(r'^dashboard', views.dashboard, name="dashboard"),
    url(r"^mypoll/", views.mypoll, name='mypoll'),
    url("^add/", views.create, name='add'),
    url("^pollistvoted/", views.listpollisvote, name='voted')
]

