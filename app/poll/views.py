from django.shortcuts import render
from .models import Poll, PollUser
# Create your views here.

def poll(request, id):
    poll = Poll.objects.get(id=id)
    return render(request, 'poll/poll.html', {'poll':poll})


def pollListView(request):
    polls = PollUser.objects.filter(user=request.user)
    print(polls)
    return render(request, 'index.html', {'polls': polls})


