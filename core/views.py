# Import necessary modules and classes
from django.shortcuts import render
from rest_framework import mixins
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework import generics
from .models import *  # Import models from the same directory
from .serializers import *  # Import serializers from the same directory
from django.contrib.auth import get_user_model
# from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings 
from django.template.loader import render_to_string

# def email(request, *args, **kwargs):
#     return render(request, "email-template.html", {})

# Define a view function called 'main_view'
def main_view(request, *args, **kwargs):
    """
    This view function renders the 'backend-home.html' template.
    """
    return render(request, "backend-home.html", {})


# Create a class-based view for listing and creating products
class ProductList(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    """
    This view class allows listing and creating Product objects.
    """

    # Queryset for Product objects
    queryset = Product.objects.all()
    
    # Serializer class for Product objects
    serializer_class = ProductSerializers
    
    # Specify the renderer class for JSON responses
    # renderer_classes = [JSONRenderer]

    def get(self, request, *args, **kwargs):
        """
        Handle GET request for listing products.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Handle POST request for creating a new product.
        """
        return self.create(request, *args, **kwargs)


# Create a class-based view for retrieving, updating, and deleting product details
class ProductDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    """
    This view class allows retrieving, updating, and deleting Product objects by ID.
    """

    # Queryset for Product objects
    queryset = Product.objects.all()
    
    # Serializer class for Product objects
    serializer_class = ProductSerializers

    def get(self, request, *args, **kwargs):
        """
        Handle GET request for retrieving product details.
        """
        return self.retrieve(request, *args, **kwargs)


# Create a class-based view for listing, creating, and deleting product images
class ProductImageList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    """
    This view class allows listing, creating, and deleting ProductImage objects.
    """

    # Queryset for ProductImage objects
    queryset = ProductImage.objects.all()
    
    # Serializer class for ProductImage objects
    serializer_class = ProductImageSerializer

    def get(self, request, *args, **kwargs):
        """
        Handle GET request for listing product images.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Handle POST request for creating a new product image.
        """
        return self.create(request, *args, **kwargs)


# Create a class-based view for retrieving and deleting product image details
class ProductImageDetail(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    """
    This view class allows retrieving and deleting ProductImage objects by ID.
    """

    # Queryset for ProductImage objects
    queryset = ProductImage.objects.all()
    
    # Serializer class for ProductImage objects
    serializer_class = ProductImageSerializer

    def get(self, request, *args, **kwargs):
        """
        Handle GET request for retrieving product image details.
        """
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Handle DELETE request for deleting a product image.
        """
        return self.destroy(request, *args, **kwargs)


# Create a class-based view for listing and creating users
class UserList(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    """
    This view class allows listing and creating User objects.
    """

    # Get the User model (custom user model if defined)
    User = get_user_model()
    
    # Queryset for User objects
    queryset = User.objects.all()
    
    # Serializer class for User objects
    serializer_class = UserSerializer
    
    # Specify the renderer class for JSON responses
    # renderer_classes = [JSONRenderer]

    def get(self, request, *args, **kwargs):
        """
        Handle GET request for listing users.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Handle POST request for creating a new user.
        """
        # Email sending
        subject = "Welcome to our store"
        message = render_to_string("email-template.html", {
            "name": request.data["username"],
            "customer_id": request.data["customer_id"],
        })
        from_email = settings.EMAIL_HOST_USER
        to_list = [request.data["email"]]
        send_mail(subject, message, from_email, to_list, fail_silently=False)
        return self.create(request, *args, **kwargs)


# Create a class-based view for retrieving, updating, and deleting user details
class UserDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    """
    This view class allows retrieving, updating, and deleting User objects by ID.
    """

    # Get the User model (custom user model if defined)
    User = get_user_model()
    
    # Queryset for User objects
    queryset = User.objects.all()
    
    # Serializer class for User objects
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        """
        Handle GET request for retrieving user details.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Handle PUT request for updating user details.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Handle DELETE request for deleting a user.
        """
        return self.destroy(request, *args, **kwargs)


# Create a class-based view for listing and creating orders
class OrderList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    """
    This view class allows listing and creating Order objects.
    """

    # Queryset for Order objects
    queryset = Order.objects.all()
    
    # Serializer class for Order objects
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        """
        Handle GET request for listing orders.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Handle POST request for creating a new order.
        """
        return self.create(request, *args, **kwargs)


# Create a class-based view for retrieving, updating, and deleting order details
class OrderDetails(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    """
    This view class allows retrieving, updating, and deleting Order objects by ID.
    """

    # Queryset for Order objects
    queryset = Order.objects.all()
    
    # Serializer class for Order objects
    serializer_class = OrderSerializer
    
    # Specify the renderer class for JSON responses
    # renderer_classes = [JSONRenderer]

    def get(self, request, *args, **kwargs):
        """
        Handle GET request for retrieving order details.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Handle PUT request for updating order details.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Handle DELETE request for deleting an order.
        """
        return self.destroy(request, *args, **kwargs)
