from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^create/", views.show_poll),
    url(r"^test/", views.test),
    url(r"^cookie/", views.set_cookie)
]
