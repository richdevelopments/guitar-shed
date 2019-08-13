from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    store = Product.objects.all()
    return render(request, "store.html", {"store": store})