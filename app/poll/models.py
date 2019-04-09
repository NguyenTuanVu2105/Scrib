from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class Poll(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    note = models.TextField()
    user_attend = models.ManyToManyField(User, through="PollUser", related_name="attend")
    date_create = models.DateTimeField(auto_now=True)
    user_create = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="create")

    class Meta:
        db_table = "poll"

    def __str__(self):
        return self.name


class PollTime(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    class Meta:
        db_table = "polltime"

    def __str__(self):
        return str.format("{0} {1} - {2}", str(self.date), str(self.start_time), str(self.end_time))


class PollUser(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_voted = models.BooleanField()

    class Meta:
        db_table = "poll_user"

    def __str__(self):
        return self.user.username


class Vote(models.Model):
    time = models.ForeignKey(PollTime, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "vote"

    def __str__(self):
        return str(self.user)