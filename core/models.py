# Import necessary modules and classes
from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from django.contrib.auth import get_user_model
from django.db.models import Sum  # Import Sum for aggregation
from .managers import CustomUserManager



# Define a custom user model by extending AbstractUser
class CustomUser(AbstractUser):
    # A UUID field for a unique customer ID
    customer_id = models.UUIDField(verbose_name="Customer ID", default=uuid4)
    # Cart field for storing products in the cart (many-to-many relationship with Product)
    cart = models.ManyToManyField("Product", blank=True)
    # Email field for authentication (unique and required)
    email = models.EmailField(verbose_name="email address", blank=False, unique=True)
    # Specify that the email field is used for authentication
    USERNAME_FIELD = "email"
    # Additional required fields during user creation
    REQUIRED_FIELDS = [
        "username",
    ]
    objects = CustomUserManager()

    def __repr__(self) -> str:
        return f"{self.customer_id} - {self.username} - {self.email}"


# Model for products available in the e-commerce platform
class Product(models.Model):
    # A UUID field for a unique product ID (primary key)
    product_id = models.UUIDField(
        verbose_name="Product ID", default=uuid4, primary_key=True, editable=False
    )
    # Name of the product
    name = models.CharField(verbose_name="Product Name", max_length=100)
    # Description of the product
    description = models.TextField(verbose_name="Product Description", max_length=500)
    # Price of the product with decimal precision
    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2)
    # Date and time when the product was added
    discount = models.IntegerField(verbose_name="Discount", default=0, blank=False, null=False, editable=True)
    
    date_added = models.DateTimeField(verbose_name="Date Added", auto_now_add=True)

    def __repr__(self) -> str:
        return f"{self.product_id} - {self.name} - {self.price}"

# Function to determine the upload path for product images
def get_upload_to(instance, filename):
    return f"Product {instance.product.product_id}/{filename}"


# Model for storing images associated with products
class ProductImage(models.Model):
    # A foreign key relationship with the Product model
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # Image field to store product images (optional, blank=True, null=True)
    image = models.ImageField(
        verbose_name="Product Image", upload_to=get_upload_to, blank=True, null=True
    )

    def __repr__(self) -> str:
        return f"Image(s) pointing to {self.product.name}"


# Model for customer orders
class Order(models.Model):
    # Choices for order status
    status = (
        ("Pending", "Pending"),
        ("Purchased", "Purchased"),
        ("In Transit", "In Transit"),
        ("Out for Delivery", "Out for Delivery"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    )
    # A UUID field for a unique order ID (primary key)
    order_id = models.UUIDField(
        verbose_name="Order ID", default=uuid4, primary_key=True, editable=False
    )
    # Foreign key relationship with the custom user model (buyer)
    buyer = models.ForeignKey(
        get_user_model(), verbose_name="Buyer", on_delete=models.SET_NULL, null=True
    )
    # Foreign key relationship with the Product model (ordered product)
    product_ordered = models.ForeignKey(
        Product, verbose_name="Product Ordered", on_delete=models.SET_NULL, null=True
    )
    # Date and time when the order was placed
    date_ordered = models.DateTimeField(verbose_name="Date Ordered", auto_now_add=True)
    # Status of the order (choices defined above)
    status = models.CharField(
        verbose_name="Status", max_length=50, choices=status, default="Pending"
    )

    # Method to calculate the total order price for a specific buyer
    def get_total_order_price(self, buyer_):
        # Calculate the total price for all orders of the given buyer
        total_price = Order.objects.filter(buyer=buyer_).aggregate(
            Sum("product_ordered__price")
        )["product_ordered__price__sum"]

        # Return the total price (or 0 if no orders found)
        return total_price or 0


class Review(models.Model):
    # A UUID field for a unique review ID (primary key)
    review_id = models.UUIDField(
        verbose_name="Review ID", default=uuid4, primary_key=True, editable=False
    )
    # Foreign key relationship with the Product model (reviewed product)
    product_reviewed = models.ForeignKey(
        Product, verbose_name="Product Reviewed", on_delete=models.SET_NULL, null=True
    )
    # Foreign key relationship with the custom user model (reviewer)
    reviewer = models.ForeignKey(
        get_user_model(), verbose_name="Reviewer", on_delete=models.SET_NULL, null=True
    )
    # Date and time when the review was added
    date_added = models.DateTimeField(verbose_name="Date Added", auto_now_add=True)
    # Review text
    review = models.TextField(verbose_name="Review", max_length=500)
    # Rating for the product
    rating = models.IntegerField(verbose_name="Rating", default=0)

    def __repr__(self) -> str:
        return f"{self.review_id} - {self.product_reviewed} - {self.reviewer} - {self.rating}"
