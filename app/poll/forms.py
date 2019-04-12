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
            'date' : forms.TextInput(attrs={
                "class": "form-control datepicker",
                "autocomplete": "off",
                "placeholder": "Ngày diễn ra"
            }),
            'start_time': forms.TextInput(attrs={
                "class": "form-control timepicker",
                "autocomplete": "off",
                "placeholder": "Thời gian bắt đầu"
            }),
            'end_time': forms.TextInput(attrs={
                "class": "form-control timepicker",
                "autocomplete": "off",
                "placeholder": "Thời gian kết thúc"
            })
        }


class VoteForm(ModelForm):
    class Meta:
        model = Vote
        fields = ['time']
        widgets = {
            'time': CheckboxSelectMultiple()
        }
