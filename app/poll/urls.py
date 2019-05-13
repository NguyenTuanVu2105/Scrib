from django.conf.urls import url

from . import views

app_name = "poll"
urlpatterns = [
    url(r"^poll/(\d+)/", views.poll, name="detail"),
    url(r"^show/", views.show, name="unvoted"),
    url(r'^dashboard', views.dashboard, name="dashboard"),
    url(r"^mypoll/", views.mypoll, name='mypoll'),
    url(r"^add/", views.create, name='add'),
    url(r"^edit/(\d+)/", views.edit, name='edit'),
    url(r"^pollistvoted/", views.listpollisvote, name='voted'),
    url(r"^delete/(\d+)/", views.delete, name="delete"),
    url(r"^json/user/", views.autocompleteUser)
]

