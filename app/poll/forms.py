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
        widgets = {
            'date' : DatePickerInput(),
            'start_time': TimePickerInput(),
            'end_time': TimePickerInput()
        }

class VoteForm(ModelForm):
    class Meta:
        model = Vote
        fields = ['time']
        widgets = {
            'time': CheckboxSelectMultiple()
        }