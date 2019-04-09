from django.shortcuts import render
from .models import Poll
# Create your views here.

def poll(request, id):
    poll = Poll.objects.get(id=id)
    return  render(request, 'poll/poll.html', {'poll':poll})