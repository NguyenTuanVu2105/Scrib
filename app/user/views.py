from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.views.generic import FormView
from django.urls import reverse, reverse_lazy

# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if not authenticate(username=username):
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect(request, r"^$")
    form = SignUpForm()
    return render(request, "user/signup.html", {"form": form})


class LoginView(FormView):
    template_name = "user/login.html"
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse_lazy("index")

    def form_valid(self, form):
        user = form.get_user()
        auth_login(self.request, user)
        return super(LoginView, self).form_valid(form)


    def form_invalid(self, form):
        response = super(LoginView, self).form_invalid(form)
        messages.error(
            self.request, 'Sai tên đăng nhập hoặc mật khẩu')
        return response