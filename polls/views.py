from django.shortcuts import render
from polls.models import VotingPoll, Option
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User

import datetime
import logging


logging.basicConfig(level=logging.INFO)

# Create your views here.
def polls(request):
    """A view that displays the polls page"""

    polls = VotingPoll.objects.all()
    user = User.objects.get(username=request.user.username)
    if request.method == "POST":
        option_id = request.POST["vote"]

        option = Option.objects.get(id=option_id)
        option.voters.add(user)
        option.save()

    logging.info("TEST")
    return render(request, 'polls.html', {'polls': polls, 'user': user})
