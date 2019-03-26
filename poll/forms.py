from django.forms import ModelForm
from .models import Poll, PollTime


class PollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['name', 'location', 'note']


class PollTimeForm(ModelForm):
    class Meta:
        model = PollTime
        fields = ['start_time', 'end_time']
