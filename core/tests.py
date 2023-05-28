from django.test import TestCase
from .models import *

# test_user = CustomUser.objects.create_user(
#     username="testuser",
#     email="test123@gmail.com",
#     password="test123zzz",
#     first_name="test",
#     last_name="user",
# )

# class CustomUserTestCase(TestCase):
#     def test_user_creation(self):
#         self.assertEqual(self.test_user.email, "test123@gmail.com", "The email address of the user is not correct")
#         self.assertEqual(self.test_user.username, "testuser", "The username of the user is not correct")
#         self.assertEqual(self.test_user.first_name, "test", "The first name of the user is not correct")
#         self.assertEqual(self.test_user.last_name, "user", "The last name of the user is not correct")
#         return CustomUser.objects.delete(email="test123@gmail.com")

class ProductTestCase(TestCase):
    test_product = Product.objects.create(
        name="test product",
        description="test product description",
        price=10.00,
    )
    def test_product_creation(self):
        self.assertEqual(self.test_product.name, "test product", "The name of the product is not correct")
        self.assertEqual(self.test_product.description, "test product description", "The description of the product is not correct")
        self.assertEqual(self.test_product.price, 10.00, "The price of the product is not correct")
        return 

class OrderTestCase(TestCase):
    test_user = CustomUser.objects.create(
        username="testuse1r",
        email="test12345@gmail.com",
        password="test123zzz",
        first_name="test",
        last_name="user",
    )
    test_product = Product.objects.create(
        name="test product",
        description="test product description",
        price=10.00,
    )
    test_order = Order.objects.create(
        buyer=test_user,
        product_ordered=test_product,
        status="Pending",
    )

    def test_order_creation(self):
        self.assertEqual(self.test_order.buyer, self.test_user, "The buyer of the order is not correct")
        self.assertEqual(self.test_order.product_ordered, self.test_product, "The product ordered of the order is not correct")
        self.assertEqual(self.test_order.status, "Pending", "The status of the order is not correct")
        return

