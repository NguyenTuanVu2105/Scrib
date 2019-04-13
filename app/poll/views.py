from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from app.core.views import LoginRequiredMixin
from django.views.generic import FormView, CreateView
from django.urls import reverse, reverse_lazy
from .models import Poll, PollTime, PollUser
from .forms import PollTimeForm, PollForm, VoteForm
# Create your views here.


def poll(request, id):
    poll = Poll.objects.get(id=id)
    dates = PollTime.objects.filter(poll=poll)
    users = PollUser.objects.filter(poll=poll)
    return render(request, 'poll/detail.html', {'poll': poll, 'dates': dates, 'users': users})


def show(request):

    # poll = PollUser.objects.all().values('poll__name', 'poll__location', 'is_voted')
    # for k in poll:
    #     print(k['poll__name'])
    #     print(type(k['is_voted']))
    # return HttpResponse(poll)
    pollusers = PollUser.objects.filter(is_voted=True)
    polls = []
    for i in range(len(pollusers)):
        polls.append(pollusers[i].poll)
    print(polls[0].note)
    return HttpResponse(polls)




def dashboard(request):
    return render(request, "poll/dashboard.html")


@login_required
def mypoll(request):
    mypolls = Poll.objects.filter(user_create_id=request.user.id)
    return render(request, 'poll/mypoll.html', {'mypolls': mypolls})


def create(request):
    if request.method == "POST":
        # --- Xu ly Poll ---
        form = PollForm(request.POST)
        if form.is_valid():
            poll = form.save(commit=False)
            poll.user_create = request.user
            poll.save()
            poll_manager = PollUser(user=request.user, poll= poll, is_voted=True)
            poll_manager.save()

            #--- Xu ly time
            cd = request.POST
            dates = cd.getlist("date")
            start_times = cd.getlist("start_time")
            end_times = cd.getlist("end_time")
            for i in range(len(dates)):
                time = PollTime(poll=poll, date=dates[i], start_time=start_times[i], end_time=end_times[i])
                time.save()
                return HttpResponseRedirect(reverse_lazy("poll:mypoll"))

    return render(request, "poll/create.html")


def listpollisvote(request):
    # listpolls = PollUser.objects.all().values('poll__name', 'poll__location', 'is_voted')
    pollusers = PollUser.objects.filter(is_voted=True)
    listpoll = Poll.objects.all()

    polls = []
    n = range(len(pollusers))
    for i in n:
        cnt = 0
        list = []
        for j in listpoll:
            if (pollusers[i].poll.name == j.name):
                cnt = cnt + 1
        list = [cnt, pollusers[i].poll.location, pollusers[i].poll.name,]
        polls.append(list)

    return render(request, 'poll/polls_is_voted.html', {'listpolls': polls})

