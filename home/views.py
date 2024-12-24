from django.shortcuts import render, get_object_or_404, redirect
from home.models import Product, PRODUCT_TYPE, STATUS


# Create your views here.

def products(request):
    # Retrieve all products from the database
    product_list = Product.objects.all()

    # Pass the products to the template
    return render(request, 'products.html', {'products': product_list})

def create_product(request):

    if request.method == "POST":
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        status = request.POST.get('status')

        # category = category.title()
        # Select Category based on value
        for pt in PRODUCT_TYPE:
            if pt[0] == category:
                category = pt[1]
                break

        # Create a new product instance and save it
        product = Product.objects.create(
            name=name,
            category=category,
            price=price,
            status=status
        )

        return redirect('products')

    return render(request, 'create-product.html', {'product_type' : PRODUCT_TYPE, 'status':STATUS})

def update_product(request, pk):

    # Find the product with id = pk
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        # Redirect to 404.html explicitly
        return render(request, '404.html', status=404)

    # if Submission happens then
    if request.method == "POST":
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        status = request.POST.get('status')

        # category = category.title()
        # Select Category based on value
        for pt in PRODUCT_TYPE:
            if pt[0] == category:
                category = pt[1]
                break

        # Update the product with the new data
        product.name = name
        product.category = category
        product.price = price
        product.status = status

        # Save the updated product to the database
        product.save()

        return redirect('products')

    return render(request, 'update-product.html', {'product':product, 'product_type' : PRODUCT_TYPE, 'status':STATUS})


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
