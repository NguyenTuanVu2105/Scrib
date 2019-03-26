from django.db import models
from user.models import UserProfile


# Create your models here.
class Poll(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    note = models.TextField()
    user = models.ManyToManyField(UserProfile, through="PollUser", related_name="attend_poll")
    date_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "poll"


class PollTime(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    class Meta:
        db_table = "polltime"


class PollUser(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    is_created_user = models.BooleanField()

    class Meta:
        db_table = "poll_user"
