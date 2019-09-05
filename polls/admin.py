from django.contrib import admin
from polls.models import Option
from polls.models import VotingPoll

admin.site.register(Option)
admin.site.register(VotingPoll)
