from django.conf.urls import url

from . import views

app_name = "poll"
urlpatterns = [
    url(r"^<int:id>/", views.poll),
    url(r"^show", views.show),
    url(r'^dashboard', views.dashboard, name="dashboard"),
    url(r"^mypoll/", views.mypoll, name='mypoll'),
    url("^add/", views.create, name='add'),
    url("^pollisvoted/", views.listpollisvote, name='voted')
]

