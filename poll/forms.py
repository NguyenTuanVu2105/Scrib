from django.forms import ModelForm, DateTimeField
from django import forms
from .models import Poll, PollTime
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
