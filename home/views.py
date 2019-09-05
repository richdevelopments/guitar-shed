from django.shortcuts import render

import logging


logging.basicConfig(level=logging.INFO)

# Create your views here.
def index2(request):
    """A view that displays the index page"""
    logging.info("TEST")
    return render(request, "index.html")