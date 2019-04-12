from django.forms import ModelForm, DateTimeField, CheckboxSelectMultiple
from django import forms
from .models import Poll, PollTime, Vote
from bootstrap_datepicker_plus import TimePickerInput, DatePickerInput

class PollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['name', 'location', 'note']
    

class PollTimeForm(ModelForm):
    class Meta:
        model = PollTime
        fields = ['date', 'start_time', 'end_time']


class VoteForm(ModelForm):
    class Meta:
        model = Vote
        fields = ['time']
        widgets = {
            'time': CheckboxSelectMultiple()
        }
