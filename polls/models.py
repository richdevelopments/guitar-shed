from django.db import models
from django.contrib.auth.models import User


class Option(models.Model):

    title = models.CharField(max_length=50, blank=False, null=False)
    voters = models.ManyToManyField(User, related_name="voters")

    def __str__(self):
        return self.title


class VotingPoll(models.Model):

    option_one = models.ForeignKey(Option, related_name='option_one',
        on_delete=models.CASCADE)
    option_two = models.ForeignKey(Option, related_name='option_two',
        on_delete=models.CASCADE)
    expiry_date = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return "{} VS {}".format(
            self.option_one.title, self.option_two.title)
