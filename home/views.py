from django.shortcuts import render, get_object_or_404, redirect
from home.models import Product, PRODUCT_TYPE, STATUS


# Create your views here.

def products(request):
    """
    Retrieve all products from the database and pass them to the template for display.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered template displaying the list of all products.
    """
    product_list = Product.objects.all()

    return render(request, 'products.html', {'products': product_list})


def create_product(request):
    """
    Handle the creation of a new product. If the request method is POST,
    it will create a new product and redirect to the product list page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered template for creating a new product or a redirect to the product list.
    """
    if request.method == "POST":
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        status = request.POST.get('status')

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

    return render(request, 'create-product.html', {'product_type': PRODUCT_TYPE, 'status': STATUS})


def update_product(request, pk):
    """
    Update an existing product based on its primary key (pk). If the request method is POST,
    the product will be updated and the user will be redirected to the product list page.

    Args:
        request: The HTTP request object.
        pk: The primary key of the product to be updated.

    Returns:
        A rendered template for updating the product or a redirect to the product list.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        # Redirect to 404.html explicitly
        return render(request, '404.html', status=404)

    if request.method == "POST":
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        status = request.POST.get('status')

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

    return render(request, 'update-product.html', {'product': product, 'product_type': PRODUCT_TYPE, 'status': STATUS})


def delete_product(request, pk):
    """
    Delete an existing product based on its primary key (pk). If the request method is POST,
    the product will be deleted and the user will be redirected to the product list page.

    Args:
        request: The HTTP request object.
        pk: The primary key of the product to be deleted.

    Returns:
        A redirect to the product list page after deletion.
    """
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
