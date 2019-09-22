from django.shortcuts import render
from polls.models import VotingPoll, Option
from django.shortcuts import get_object_or_404
from django.urls import reverse

import logging


logging.basicConfig(level=logging.INFO)

# Create your views here.
def polls(request):
    """A view that displays the polls page"""

    polls = VotingPoll.objects.all()

    logging.info("TEST")
    return render(request, 'polls.html', {'polls': polls})


def vote(request):
    polls = get_object_or_404(VotingPolls, pk=polls_id)
    try:
        selected_options = polls.options_set.get(pk=request.POST['options'])
    except (KeyError, Options.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls.html', {
            'polls': polls,
            'error_message': "You didn't select an option.",
        })
    else:
        selected_options.votes += 1
        selected_options.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(polls.id,)))


def results(request):
    polls = get_object_or_404(polls, pk=polls_id)
    return render(request, 'polls/polls.html', {'polls': polls})