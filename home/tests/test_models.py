from django.test import TestCase
from ..models import PRODUCT_TYPE, STATUS, Product

class TestProductModels(TestCase):

    def test_str_method(self):
        """Test the __str__ method of the Product model."""
        product = Product.objects.create(
            name="Test Product",
            price=99.99,
            status=STATUS[1][0],  # 1 (Available)
            category=PRODUCT_TYPE[0][1]  # Electronics
        )
        self.assertEqual(str(product), "Test Product [Electronics]")