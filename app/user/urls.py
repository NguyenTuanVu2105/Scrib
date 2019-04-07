from django.conf.urls import url

from . import views

app_name = 'user'
urlpatterns = [
    url(r'^signup/', views.SignUpView.as_view(), name="signup"),
    url(r'^login/', views.LoginView.as_view(), name="login"),
]
