from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from app.core.views import LoginRequiredMixin
from django.views.generic import FormView, CreateView
from django.urls import reverse, reverse_lazy
from .models import Poll, PollTime, PollUser, Vote
from django.contrib.auth.models import User
from .forms import PollTimeForm, PollForm, VoteForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
import json
# Create your views here.

@csrf_exempt
@login_required
def poll(request, id):
    poll = Poll.objects.get(id=id)
    current_site = get_current_site(request)

    if request.is_ajax():
        #---Chuc nang Moi tham gia cuoc hop---
        emails = request.POST.get('users_invited')
        emails = str(emails).split(", ")
        send_mail("Thư mời tham gia cuộc họp", "Tham gia cuộc họp theo đường dẫn sau: " + current_site.domain +"/poll/" + id,
                  "scribteam123@gmail.com", [emails], fail_silently=False)
        for email in emails:
            user = User.objects.get(email = email)
            poll_user = PollUser(user = user, poll = poll, is_voted = False)
            poll_user.save()

    datetimes = PollTime.objects.filter(poll=poll)
    users = PollUser.objects.filter(poll=poll)
    votes = Vote.objects.filter(time__poll=poll)
    return render(request, 'poll/detail.html', {'poll': poll, 'datetimes': datetimes, 'users': users, 'votes': votes})


def show(request):
    pollusers = PollUser.objects.filter(is_voted=True)
    polls = []
    for polluser in pollusers:
        polls.append(polluser.poll)
    return HttpResponse(polls)




def dashboard(request):
    mypolls = Poll.objects.filter(user_create=request.user)
    number_user_attends = {}
    number_user_voted = {}
    for poll in mypolls:
        user_attend = PollUser.objects.filter(poll=poll)
        user_voted = PollUser.objects.filter(poll=poll, is_voted=True)
        number_user_attends[poll.id] = len(user_attend)
        number_user_voted[poll.id] = len(user_voted)

    pollusers = PollUser.objects.filter(user=request.user)
    attend_poll = []
    for polluser in pollusers:
        if polluser.poll.user_create != request.user:
            attend_poll.append(polluser.poll)
    attend_number_user_attends = {}
    attend_number_user_voted = {}
    for poll in attend_poll:
        user_attend = PollUser.objects.filter(poll=poll)
        user_voted = PollUser.objects.filter(poll=poll, is_voted=True)
        attend_number_user_attends[poll.id] = len(user_attend)
        attend_number_user_voted[poll.id] = len(user_voted)

    return render(request, "poll/dashboard.html", {
        'mypolls': mypolls,
        'number_user_attends': number_user_attends,
        'number_user_voted': number_user_voted,
        'attend_polls': attend_poll,
        'attend_number_user_attends': attend_number_user_attends,
        'attend_number_user_voted': attend_number_user_voted,
    })



def mypoll(request):
    poll_users = PollUser.objects.filter(user=request.user)
    polls = [x.poll for x in poll_users]
    number_user_attends = {}
    number_user_voted = {}
    for poll in polls:
        user_attend = PollUser.objects.filter(poll=poll)
        user_voted = PollUser.objects.filter(poll=poll, is_voted=True)
        number_user_attends[poll.id] = len(user_attend)
        number_user_voted[poll.id] = len(user_voted)
    return render(request, 'poll/mypoll.html', {'polls': polls, 'number_user_attends': number_user_attends, 'number_user_voted': number_user_voted,})



def create(request):
    if request.method == "POST":
        # --- Xu ly Poll ---
        form = PollForm(request.POST)
        if form.is_valid():
            poll = form.save(commit=False)
            poll.user_create = request.user
            poll.save()

            poll_manager = PollUser(user=request.user, poll=poll, is_voted=True)
            poll_manager.save()

            #--- Xu ly time ---
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


def edit(request, id):
    poll = Poll.objects.get(id=id)
    times = PollTime.objects.filter(poll=poll)
    if request.method == "GET":
        return render(request, "poll/edit.html", {'poll': poll, 'times': times})
    elif request.method == "POST":
            # --- Xu ly Poll ---
            cd = request.POST
            poll.name = cd.get('name')
            poll.location = cd.get('location')
            poll.note = cd.get('note')
            poll.save()
            #--- Xu ly time
            for time in times:
                time.delete()
            dates = cd.getlist("date")
            start_times = cd.getlist("start_time")
            end_times = cd.getlist("end_time")
            for i in range(len(dates)):
                time = PollTime(poll=poll, date=dates[i], start_time=start_times[i], end_time=end_times[i])
                time.save()
            return HttpResponseRedirect(reverse_lazy("poll:mypoll"))


def delete(request, id):
    poll = get_object_or_404(Poll, id=id)
    poll.delete()
    return HttpResponseRedirect(reverse_lazy("poll:mypoll"))


def autocompleteUser(request):
    if request.is_ajax():
        queryset = User.objects.all()
        list = []
        for i in queryset:
            list.append(i.email)
        data = {
            'list': list,
        }
        return JsonResponse(data)
