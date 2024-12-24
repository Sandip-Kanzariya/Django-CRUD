from django.db import models

PRODUCT_TYPE = (
    ('electronics', 'Electronics'),
    ('medical', 'Medical'),
    ('fashion', 'Fashion'),
    ('food', 'Food'),
    ('books', 'Books'),
    ('sports', 'Sports')
)

STATUS = (
    (0, 'Unavailable'),
    (1, 'Available'),
)

# Create your models here.
class Product(models.Model):
    """
    Product model representing products of different categories
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(choices=STATUS, default=1)
    category = models.CharField(choices=PRODUCT_TYPE, max_length=200)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        """
            Returns a string representation of the Product instance.

            The string format is: "<name> [<category>]"

            Returns:
                str: A string that represents the product with its name and category.

            Example:
                product = Product.objects.create(
                    name="Test Product",
                    category="Electronics",
                    price=100.00,
                    status=1
                )
                print(product)
            Output: Test Product [Electronics]

        """
        return f"{self.name} [{self.category}]"