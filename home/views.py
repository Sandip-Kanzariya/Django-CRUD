from django.shortcuts import render, get_object_or_404, redirect
from home.models import Product

# Create your views here.

def products(request):
    # Retrieve all products from the database
    product_list = Product.objects.all()

    # Pass the products to the template
    return render(request, 'products.html', {'products': product_list})

def update_product(request, pk):
    # Find the product with id = pk
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        # Redirect to 404.html explicitly
        return render(request, '404.html', status=404)

    return render(request, 'update-product.html', {'product':product})


def delete_product(request, pk):

    # Find the product with id = pk
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        # Redirect to 404.html explicitly
        return render(request, '404.html', status=404)

    if request.method == "POST":
        product.delete()
        return redirect('products')
    else:
        return redirect('products')
