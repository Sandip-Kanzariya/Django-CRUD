from django.shortcuts import render
from home.models import Product

# Create your views here.

def products(request):
    # Retrieve all products from the database
    product_list = Product.objects.all()

    # Pass the products to the template
    return render(request, 'products.html', {'products': product_list})
