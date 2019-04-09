from django.shortcuts import render
from .models import Poll
from .models import PollUser
from django.http import HttpResponse
# Create your views here.

def poll(request, id):
    poll = Poll.objects.get(id=id)
    return  render(request, 'poll/poll.html', {'poll': poll})


def show(request):
    poll = PollUser.objects.get(user=request.user).poll
    return HttpResponse(poll)


def dashboard(request):
    return render(request, "poll/dashboard.html")