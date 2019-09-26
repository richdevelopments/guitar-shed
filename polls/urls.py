from django.conf.urls import url
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from polls.models import VotingPoll, Option

from . import views

urlpatterns = [
    url(r'', views.polls, name='polls')
]