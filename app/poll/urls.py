from django.conf.urls import url

from . import views

app_name = "poll"
urlpatterns = [
    url(r"^<int:id>/", views.poll)
]
