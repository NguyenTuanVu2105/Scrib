from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
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
        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request, "You've signed up successfully,\
                                You can log in now.")
        return redirect(request, "")


def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username, password)
        if user:
            login(username, password)
            return redirect(request, "")

