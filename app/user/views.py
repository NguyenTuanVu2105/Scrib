from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.views.generic import FormView, CreateView
from django.urls import reverse, reverse_lazy
from django.core.mail import send_mail
# Create your views here.


def get_user(email):
    try:
        return User.objects.get(email=email.lower())
    except User.DoesNotExist:
        return None


class SignUpView(CreateView):
    template_name = "user/signup.html"
    model = User
    success_url = reverse_lazy("user:login")
    form_class = SignUpForm

    def get_success_url(self):
        return reverse_lazy("user:login")

    def form_valid(self, form):
        active = 'abdbNojjhf3984'
        send_mail('Activate account', 'Đây là mã xác nhận của bạn: ' + active, 'scribteam123@gmail.com',
                  ['lemaian034@gmail.com'], fail_silently=False)
        form.save()
        messages.success(self.request, "Bạn đã đăng ký thành công. Xin mời đăng nhập")
        return HttpResponseRedirect(self.get_success_url())


class LoginView(FormView):
    template_name = "user/login.html"
    form_class = AuthenticationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', False)
        return context

    def get_success_url(self):
        nextlink = self.request.POST.get('next', False)
        if nextlink:
            return nextlink
        return reverse_lazy("poll:dashboard")

    def form_valid(self, form):
        user = form.get_user()
        auth_login(self.request, user)
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        response = super(LoginView, self).form_invalid(form)
        messages.error(
            self.request, 'Sai tên đăng nhập hoặc mật khẩu')
        return response


