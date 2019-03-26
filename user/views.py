from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from user.forms import UserForm
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if not authenticate(username=username):
            user = User.objects.create_user(username, email, password)
            user.save()
            messages.success(request, "You've signed up successfully,\
                                You can log in now.")
            return redirect(request, r"^$")
    form = UserForm()
    return render(request, "user/signup.html", {"form": form})


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(request, r"^$")
    form = UserForm()
    return render(request, "user/signin.html", {"form": form})
