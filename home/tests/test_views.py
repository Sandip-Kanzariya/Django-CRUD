from django.test import TestCase, Client
from django.urls import reverse
from ..models import Product, PRODUCT_TYPE, STATUS

class TestProductViews(TestCase):

    def setUp(self):
        """Set up reusable test data."""
        self.client = Client()

        self.products_url = reverse('products')
        self.create_product_url = reverse('create_product')


    def test_products_GET(self):
        """Test the GET request to the 'products' view."""
        response = self.client.get(self.products_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')

    def test_create_product_POST_adds_new_product(self):
        """Test the POST request to 'create_product' to add a new product."""
        response = self.client.post(self.create_product_url, {
            'name': 'Banana Chips',
            'category': PRODUCT_TYPE[3][1],  # Using 'Food' as category
            'price': '10.50',
            'status': STATUS[1][0],  # Using 'Available' as status
        })

        # Assert that the product was created
        self.assertEquals(Product.objects.count(), 1)
        product = Product.objects.first()
        self.assertEquals(product.name, 'Banana Chips')
        self.assertEquals(product.category, PRODUCT_TYPE[3][1])  # 'Food'
        self.assertEquals(product.price, 10.50)
        self.assertEquals(product.status, STATUS[1][0])  # 1 (Available)

        # Assert redirection to the products page
        self.assertRedirects(response, self.products_url)

