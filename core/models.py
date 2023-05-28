from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    customer_id = models.UUIDField(verbose_name="Customer ID", default=uuid4)
    email = models.EmailField(verbose_name="email address", blank=False, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username",]

    def __repr__(self) -> str:
        return f"{self.customer_id} - {self.username} - {self.email}"

class Product(models.Model):
    """The model responsible for holding the data for the products"""
    product_id = models.UUIDField(verbose_name="Product ID", default=uuid4, primary_key=True, editable=False)
    name = models.CharField(verbose_name="Product Name", max_length=100)
    description = models.TextField(verbose_name="Product Description", max_length=500)
    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2)
    # image = models.ImageField(verbose_name="Product Image", upload_to="product_images", blank=True, null=True)
    date_added = models.DateTimeField(verbose_name="Date Added", auto_now_add=True)

    def __repr__(self) -> str:
        return f"{self.product_id} - {self.name} - {self.price}"

class Order(models.Model):
    status = (
        ("Pending", "Pending"),
        ("Purchased", "Purchased"),
        ("In Transit", "In Transit"),
        ("Out for Delivery", "Out for Delivery"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    )

    order_id = models.UUIDField(verbose_name="Order ID", default=uuid4, primary_key=True, editable=False)
    buyer = models.ForeignKey(get_user_model(), verbose_name="Buyer", on_delete=models.SET_NULL, null=True)
    product_ordered = models.ForeignKey(Product, verbose_name="Product Ordered", on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateTimeField(verbose_name="Date Ordered", auto_now_add=True)
    status = models.CharField(verbose_name="Status", max_length=50, choices=status, default="Pending")

    # def get_total_order_price(self, buyer_):
    #     return self.objects.all(buyer=buyer_).aggregate(models.Sum("product_ordered__price"))