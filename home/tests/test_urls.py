from django.urls import resolve, reverse
from django.test import SimpleTestCase
from ..views import products, create_product, update_product, delete_product


class TestUrls(SimpleTestCase):
    """Tests for URL resolution in the application."""

    def test_products_url_resolves(self):
        """Test that the 'products' URL resolves to the correct view."""
        url = reverse('products')  # Generate the URL for the 'products' route
        self.assertEquals(resolve(url).func, products)  # Assert the resolved view is correct

    def test_create_product_url_resolves(self):
        """Test that the 'create_product' URL resolves to the correct view."""
        url = reverse('create_product')  # Generate the URL for the 'create_product' route
        self.assertEquals(resolve(url).func, create_product)  # Assert the resolved view is correct

    def test_update_product_url_resolves(self):
        """Test that the 'update_product' URL resolves to the correct view."""
        url = reverse('update_product', args=[2])  # Generate the URL with pk=2
        self.assertEquals(resolve(url).func, update_product)  # Assert the resolved view is correct

    def test_delete_product_url_resolves(self):
        """Test that the 'delete_product' URL resolves to the correct view."""
        url = reverse('delete_product', args=[2])  # Generate the URL with pk=2
        self.assertEquals(resolve(url).func, delete_product)  # Assert the resolved view is correct
