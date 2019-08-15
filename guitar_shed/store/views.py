from django.shortcuts import render
from store.models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "store.html", {"products": products})