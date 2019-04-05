from django.shortcuts import render
from .forms import PollForm, PollTimeForm
# Create your views here.


def creat_poll(request):
    form = PollForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PollForm()

    context = {
        'form': form
    }
    return render(request, 'poll/creat_poll.html', context)
