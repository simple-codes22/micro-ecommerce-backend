from django.test import TestCase
from .models import *


# Test case for the CustomUser model
class CustomUserTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.test_user = CustomUser.objects.create(
            username="testuser",
            email="test123@gmail.com",
            password="test123zzz",
            first_name="test",
            last_name="user",
        )

    def test_user_creation(self):
        # Check if the user attributes match the expected values
        self.assertEqual(
            self.test_user.email,
            "test123@gmail.com",
            "The email address of the user is not correct",
        )
        self.assertEqual(
            self.test_user.username,
            "testuser",
            "The username of the user is not correct",
        )
        self.assertEqual(
            self.test_user.first_name,
            "test",
            "The first name of the user is not correct",
        )
        self.assertEqual(
            self.test_user.last_name, "user", "The last name of the user is not correct"
        )


# Test case for the Product model
class ProductTestCase(TestCase):
    def setUp(self):
        # Create a test product
        self.test_product = Product.objects.create(
            name="test product",
            description="test product description",
            price=10.00,
        )

    def test_product_creation(self):
        # Check if the product attributes match the expected values
        self.assertEqual(
            self.test_product.name,
            "test product",
            "The name of the product is not correct",
        )
        self.assertEqual(
            self.test_product.description,
            "test product description",
            "The description of the product is not correct",
        )
        self.assertEqual(
            self.test_product.price, 10.00, "The price of the product is not correct"
        )


# Test case for the ProductImage model
class ProductImageTestCase(TestCase):
    def setUp(self):
        # Create a test product
        self.test_product = Product.objects.create(
            name="test product",
            description="test product description",
            price=10.00,
        )
        # Create a test product image
        self.test_product_image = ProductImage.objects.create(
            product=self.test_product,
            image="test_image.jpg",  # Replace with an actual image file path or use Django's File objects for testing.
        )

    def test_product_image_creation(self):
        # Check if the product image attributes match the expected values
        self.assertEqual(
            self.test_product_image.product,
            self.test_product,
            "The product of the product image is not correct",
        )
        self.assertEqual(
            self.test_product_image.image,
            "test_image.jpg",
            "The image path of the product image is not correct",
        )


# Test case for the Order model
class OrderTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.test_user = CustomUser.objects.create(
            username="testuse1r",
            email="test12345@gmail.com",
            password="test123zzz",
            first_name="test",
            last_name="user",
        )
        # Create a test product
        self.test_product = Product.objects.create(
            name="test product",
            description="test product description",
            price=10.00,
        )
        # Create a test order
        self.test_order = Order.objects.create(
            buyer=self.test_user,
            product_ordered=self.test_product,
            status="Pending",
        )

    def test_order_creation(self):
        # Check if the order attributes match the expected values
        self.assertEqual(
            self.test_order.buyer,
            self.test_user,
            "The buyer of the order is not correct",
        )
        self.assertEqual(
            self.test_order.product_ordered,
            self.test_product,
            "The product ordered of the order is not correct",
        )
        self.assertEqual(
            self.test_order.status, "Pending", "The status of the order is not correct"
        )
