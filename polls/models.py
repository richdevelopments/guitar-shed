from django.db import models


class Option(models.Model):

    title = models.CharField(max_length=50, blank=False, null=False)
    number_of_votes = models.IntegerField()

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
