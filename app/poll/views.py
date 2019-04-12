from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from app.core.views import LoginRequiredMixin
from django.views.generic import FormView, CreateView
from django.urls import reverse, reverse_lazy
from .models import Poll, PollTime, PollUser
from .forms import PollTimeForm, PollForm
# Create your views here.


def poll(request, id):
    poll = Poll.objects.get(id=id)
    return  render(request, 'poll/poll.html', {'poll': poll})


def show(request):
    poll = PollUser.objects.all().values('poll__name', 'poll__location', 'is_voted')
    for k in poll:
        print(k['poll__name'])
        print(type(k['is_voted']))
    return HttpResponse(poll)


def dashboard(request):
    return render(request, "poll/dashboard.html")


@login_required
def mypoll(request):
    mypolls = Poll.objects.filter(user_create_id=request.user.id)
    return render(request, 'poll/mypoll.html', {'mypolls': mypolls})


def create(request):
    return render(request, "poll/create.html")


def listpollisvote(request):
    listpolls = PollUser.objects.all().values('poll__name', 'poll__location', 'is_voted')
    return render(request, 'poll/polls_is_voted.html', {'listpolls': listpolls})
