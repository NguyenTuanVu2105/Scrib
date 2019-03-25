from django.db import models
from user.models import UserProfile


# Create your models here.
class Poll(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    note = models.TextField()
    user_attend = models.ManyToManyField(UserProfile, related_name="attend_poll")
    user_create = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="create_poll")
    date_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "poll"


class PollTime(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    class Meta:
        db_table = "polltime"
