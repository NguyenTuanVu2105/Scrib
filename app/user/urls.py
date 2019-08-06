from django.conf.urls import url, include

from . import views
from django.contrib.auth.views import LogoutView

app_name = 'user'
urlpatterns = [
    url(r'^signup/', views.SignUpView.as_view(), name="signup"),
    url(r'^login/', views.LoginView.as_view(), name="login"),
    url(r'^logout/', LogoutView.as_view(), name="logout"),
    url(r'^activate/', views.activate, name="activate"),
    url(r'^webhook/', views.webhook, name='webhook'),
    url(r'^log/', views.log, name='webhook')
]
