from django.shortcuts import render
from store.models import Product

# Create your views here.
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "store.html", {"products": products})