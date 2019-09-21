from django.shortcuts import render
from polls.models import VotingPoll, Option

import logging


logging.basicConfig(level=logging.INFO)

# Create your views here.
def polls(request):
    """A view that displays the polls page"""

    polls = VotingPoll.objects.all()

    logging.info("TEST")
    return render(request, 'polls.html', {'polls': polls})


