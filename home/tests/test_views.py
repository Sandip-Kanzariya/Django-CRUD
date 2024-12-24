from django.test import TestCase, Client
from django.urls import reverse
from ..models import Product, PRODUCT_TYPE, STATUS

class TestProductViews(TestCase):

    # Automatic invocation
    def setUp(self):
        """Set up reusable test data."""
        self.client = Client()
        self.product = Product.objects.create(
            name="Test Product",
            category="Electronics",
            price=100.00,
            status=1
        )
        self.products_url = reverse('products')
        self.create_product_url = reverse('create_product')
        self.update_url = reverse('update_product', args=[self.product.id]) # Check for added product in setUp
        self.delete_url = reverse('delete_product', args=[self.product.id]) # Check for added product in setUp

    # So, it not conflict with state of previous test case
    def tearDown(self):
        """Clean up after each test."""
        Product.objects.all().delete()

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
        self.assertEquals(Product.objects.count(), 2)  # 1 product from setUp() + new one

        # Fetch the newly created product
        product = Product.objects.exclude(id=self.product.id).first()  # Exclude the initial product created in setUp

        self.assertEquals(product.name, 'Banana Chips')
        self.assertEquals(product.category, PRODUCT_TYPE[3][1])  # 'Food'
        self.assertEquals(product.price, 10.50)
        self.assertEquals(product.status, STATUS[1][0])  # 1 (Available)

        # Assert redirection to the products page
        self.assertRedirects(response, self.products_url)

    def test_update_product_GET(self):
        """Test the GET request to 'update_product' to update product"""
        response = self.client.get(self.update_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'update-product.html')

    def test_update_product_POST_valid_data(self):
        """Test the POST request to 'update_product' to update product"""
        response = self.client.post(self.update_url, {
            'name': 'Updated Product',
            'category': 'Fashion',
            'price': 150.00,
            'status': 0
        })

        # Refresh the product from the database to get the updated values
        self.product.refresh_from_db()

        self.assertEquals(response.status_code, 302)  # Redirect to products
        self.assertEquals(self.product.name, 'Updated Product')
        self.assertEquals(self.product.category, 'Fashion')  # Human-readable category
        self.assertEquals(self.product.price, 150.00)
        self.assertEquals(self.product.status, 0)

    def test_update_product_POST_invalid_product(self):
        """Test the POST request to 'update_product' to update product which is not exist."""
        invalid_update_url = reverse('update_product', args=[999])
        response = self.client.post(invalid_update_url, {
            'name': 'Invalid Product',
            'category': 'Fashion',
            'price': 150.00,
            'status': 0
        })

        self.assertEquals(response.status_code, 404) # Page not found
        self.assertTemplateUsed(response, '404.html')

    def test_delete_product_GET(self):
        """Test the GET request to 'delete_product' to delete product"""
        response = self.client.get(self.delete_url)
        self.assertEquals(response.status_code, 302)  # Redirects to products
        self.assertTrue(Product.objects.filter(id=self.product.id).exists())

    def test_delete_product_POST(self):
        """Test the POST request to 'delete_product' to delete product"""
        response = self.client.post(self.delete_url)
        self.assertEquals(response.status_code, 302)  # Redirects to products
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())

    def test_delete_product_invalid_id(self):
        """Test the request to 'delete_product' to delete product which is not exist."""
        invalid_delete_url = reverse('delete_product', args=[999])
        response = self.client.post(invalid_delete_url)
        self.assertEquals(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
