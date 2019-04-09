from django.contrib import admin
from .models import Poll, PollTime, PollUser, Vote

# Register your models here.
admin.site.register(Poll)
admin.site.register(PollTime)
admin.site.register(PollUser)
admin.site.register(Vote)