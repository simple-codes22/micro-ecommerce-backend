from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ViewSet
from.serializers import *
from .models import *


# Define a view function called 'main_view'
def main_view(request, *args, **kwargs):
    """
    This view function renders the 'backend-home.html' template.
    """
    return render(request, "backend-home.html", {})



class ProductListViewset(ViewSet):
    
    renderer_classes = [JSONRenderer]

    def list(self, request,):
        queryset = Product.objects.all()
        serializer = ProductSerializers(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, product_id=None,):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, product_id=product_id)
        serializer = ProductSerializers(product)
        return Response(serializer.data)
    # def create(self, request, )


class UserListViewSet(ViewSet):
    renderer_classes = [JSONRenderer]
    User = get_user_model()
    def list(self, request):
        queryset = self.User.objects.all()
        serializer = [user.username for user in queryset]
        return Response(serializer)

    def retrieve(self, request, username=None, password=None):
        queryset = self.User.objects.all()
        user = get_object_or_404(queryset, username=username)
        try:
            if user.check_password(password):
                serializer = UserSerializer(user)
                return Response(serializer.data)
        except Exception:
            return print("Did Not Work: ", Exception)
        serializer = UserSerializer(user)
        return Response(serializer.data)
        

class ProductImageListViewSet(ViewSet):
    def list(self, request):
        queryset = ProductImage.objects.all()
        serializer = ProductImageSerializer(queryset)
        return Response(serializer.data)
    
    def retrieve(self, request, product_id=None):
        queryset = ProductImage.objects.filter(product__id=product_id)
        serializer = ProductImageSerializer(queryset)
        return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     return


class OrderListViewSet(ViewSet):
    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset)
        return Response(serializer.data)
    
    def retrieve(self, request, product_id=None):
        queryset = Order.objects.filter(product_ordered__product_id= product_id)
        serializer = OrderSerializer(queryset)
        return Response(serializer.data)

class ReviewViewSet(ViewSet):
    def list(self, request):
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset)
        return Response(serializer.data)

    def retrieve(self, request, product_id=None):
        queryset = Order.objects.filter(product_reviewed__product_id=product_id)
        serializer = ReviewSerializer(queryset)
        return Response(serializer.data)



























# # Import necessary modules and classes
# from django.shortcuts import render
# from rest_framework import mixins
# from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
# from rest_framework import generics
# from .models import *  # Import models from the same directory
# from .serializers import *  # Import serializers from the same directory
# from django.contrib.auth import get_user_model
# from django.urls import reverse
# from rest_framework.permissions import IsAdminUser
# from rest_framework.views import APIView
# from rest_framework.response import Response


# # Define a view function called 'main_view'
# def main_view(request, *args, **kwargs):
#     """
#     This view function renders the 'backend-home.html' template.
#     """
#     return render(request, "backend-home.html", {})


# # Create a class-based view for listing and creating products
# class ProductList(
#     mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
# ):
#     """
#     This view class allows listing and creating Product objects.
#     """

#     # Queryset for Product objects
#     queryset = Product.objects.all()
    
#     # Serializer class for Product objects
#     serializer_class = ProductSerializers
    
#     # Specify the renderer class for JSON responses
#     renderer_classes = [JSONRenderer]

#     def get(self, request, *args, **kwargs):
#         """
#         Handle GET request for listing products.
#         """
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         """
#         Handle POST request for creating a new product.
#         """
#         return self.create(request, *args, **kwargs)


# # Create a class-based view for retrieving, updating, and deleting product details
# class ProductDetail(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView,
# ):
#     """
#     This view class allows retrieving, updating, and deleting Product objects by ID.
#     """

#     # Queryset for Product objects
#     queryset = Product.objects.all()
    
#     # Serializer class for Product objects
#     serializer_class = ProductSerializers

#     def get(self, request, *args, **kwargs):
#         """
#         Handle GET request for retrieving product details.
#         """
#         return self.retrieve(request, *args, **kwargs)


# # Create a class-based view for listing, creating, and deleting product images
# class ProductImageList(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView,
# ):
#     """
#     This view class allows listing, creating, and deleting ProductImage objects.
#     """

#     # Queryset for ProductImage objects
#     queryset = ProductImage.objects.all()
    
#     # Serializer class for ProductImage objects
#     serializer_class = ProductImageSerializer

#     def get(self, request, *args, **kwargs):
#         """
#         Handle GET request for listing product images.
#         """
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         """
#         Handle POST request for creating a new product image.
#         """
#         return self.create(request, *args, **kwargs)


# # Create a class-based view for retrieving and deleting product image details
# class ProductImageDetail(
#     mixins.RetrieveModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView,
# ):
#     """
#     This view class allows retrieving and deleting ProductImage objects by ID.
#     """

#     # Queryset for ProductImage objects
#     queryset = ProductImage.objects.all()
    
#     # Serializer class for ProductImage objects
#     serializer_class = ProductImageSerializer

#     def get(self, request, *args, **kwargs):
#         """
#         Handle GET request for retrieving product image details.
#         """
#         return self.retrieve(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         """
#         Handle DELETE request for deleting a product image.
#         """
#         return self.destroy(request, *args, **kwargs)

# class UserList(
#     mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
# ):
#     """
#     This view class allows listing and creating User objects.
#     """

#     # Get the User model (custom user model if defined)
#     User = get_user_model()
    
#     # Queryset for User objects
#     queryset = User.objects.all()
    
#     # Serializer class for User objects
#     serializer_class = UserSerializer
#     permission_classes = [IsAdminUser]
    
#     # Specify the renderer class for JSON responses
#     # renderer_classes = [JSONRenderer]

#     def get(self, request, *args, **kwargs):
#         """
#         Handle GET request for listing users.
#         """
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         """
#         Handle POST request for creating a new user.
#         """
#         return self.create(request, *args, **kwargs)

# class UserCreate(
#     mixins.CreateModelMixin,
#     generics.GenericAPIView
# ):
#     User = get_user_model()
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# # class UserDetail(APIView):
# #     User = get_user_model()
# #     # queryset = User.objects.all()
# #     serializer_class = UserSerializer
# #     renderer_classes = [JSONRenderer]

# #     def get(self, request, *args, **kwargs):
# #         return self.retrieve(request, *args, **kwargs)
    
# #     def retrieve(self, request, *args, **kwargs):
# #         email = kwargs.get('email')
# #         password = kwargs.get('password')
# #         user = User.objects.filter(email=email, password=password)
# #         serializer = UserSerializer(user, many=True)
# #         return Response(serializer.data)
# #     # To continue later

# # class UserDetail(
# #     generics.GenericAPIView,
# #     mixins.RetrieveModelMixin,
# #     mixins.UpdateModelMixin
# #     # mixins.CreateModelMixin,
# # ):
# #     User = get_user_model()
# #     queryset = User.objects.all()
# #     serializer_class = UserSerializer
# #     renderer_classes = [JSONRenderer]

# #     # lookup_field = 'email'
# #     lookup_url_kwarg = ['email', 'password']

# #     def get(self, request, *args, **kwargs):
# #         return self.retrieve(request, *args, **kwargs)
#     # def put(self, request, *args, **kwargs):
#     #     return self.update(request, *args, **kwargs)

# # Create a class-based view for listing and creating users
# # class UserList(
# #     mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView
# # ):
# #     """
# #     This view class allows listing and creating User objects.
# #     """

# #     # Get the User model (custom user model if defined)
# #     User = get_user_model()
    
# #     # Queryset for User objects
# #     queryset = User.objects.all()
    
# #     # Serializer class for User objects
# #     serializer_class = UserSerializer
    
# #     # Specify the renderer class for JSON responses
# #     # renderer_classes = [JSONRenderer]

# #     def get(self, request, *args, **kwargs):
# #         """
# #         Handle GET request for listing users.
# #         """
# #         return self.list(request, *args, **kwargs)

# #     def post(self, request, *args, **kwargs):
# #         """
# #         Handle POST request for creating a new user.
# #         """
# #         return self.create(request, *args, **kwargs)


# # # Create a class-based view for retrieving, updating, and deleting user details
# # class UserDetail(
# #     mixins.RetrieveModelMixin,
# #     mixins.UpdateModelMixin,
# #     mixins.DestroyModelMixin,
# #     generics.GenericAPIView,
# # ):
# #     """
# #     This view class allows retrieving, updating, and deleting User objects by ID.
# #     """

# #     # Get the User model (custom user model if defined)
# #     User = get_user_model()
    
# #     # Queryset for User objects
# #     queryset = User.objects.all()
    
# #     # Serializer class for User objects
# #     serializer_class = UserSerializer

# #     def get(self, request, *args, **kwargs):
# #         """
# #         Handle GET request for retrieving user details.
# #         """
# #         return self.retrieve(request, *args, **kwargs)

# #     def put(self, request, *args, **kwargs):
# #         """
# #         Handle PUT request for updating user details.
# #         """
# #         return self.update(request, *args, **kwargs)

# #     def delete(self, request, *args, **kwargs):
# #         """
# #         Handle DELETE request for deleting a user.
# #         """
# #         return self.destroy(request, *args, **kwargs)


# # Create a class-based view for listing and creating orders
# class OrderList(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     generics.GenericAPIView,
# ):
#     """
#     This view class allows listing and creating Order objects.
#     """

#     # Queryset for Order objects
#     queryset = Order.objects.all()
    
#     # Serializer class for Order objects
#     serializer_class = OrderSerializer

#     def get(self, request, *args, **kwargs):
#         """
#         Handle GET request for listing orders.
#         """
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         """
#         Handle POST request for creating a new order.
#         """
#         return self.create(request, *args, **kwargs)


# # Create a class-based view for retrieving, updating, and deleting order details
# class OrderDetails(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView,
# ):
#     """
#     This view class allows retrieving, updating, and deleting Order objects by ID.
#     """

#     # Queryset for Order objects
#     queryset = Order.objects.all()
    
#     # Serializer class for Order objects
#     serializer_class = OrderSerializer
    
#     # Specify the renderer class for JSON responses
#     renderer_classes = [JSONRenderer]

#     def get(self, request, *args, **kwargs):
#         """
#         Handle GET request for retrieving order details.
#         """
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         """
#         Handle PUT request for updating order details.
#         """
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         """
#         Handle DELETE request for deleting an order.
#         """
#         return self.destroy(request, *args, **kwargs)



# class ReviewList(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     generics.GenericAPIView,
# ):
#     """
#     This view class allows listing and creating Review objects.
#     """

#     # Queryset for Review objects
#     queryset = Review.objects.all()
    
#     # Serializer class for Review objects
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         """
#         Handle GET request for listing reviews.
#         """
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         """
#         Handle POST request for creating a new review.
#         """
#         return self.create(request, *args, **kwargs)

# class ReviewDetails(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView,
# ):
#     """
#     This view class allows retrieving, updating, and deleting Review objects by ID.
#     """

#     # Queryset for Review objects
#     queryset = Review.objects.all()
    
#     # Serializer class for Review objects
#     serializer_class = ReviewSerializer
    
#     # Specify the renderer class for JSON responses
#     # renderer_classes = [JSONRenderer]

#     def get(self, request, *args, **kwargs):
#         """
#         Handle GET request for retrieving review details.
#         """
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         """
#         Handle PUT request for updating review details.
#         """
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         """
#         Handle DELETE request for deleting a review.
#         """
#         return self.destroy(request, *args, **kwargs)

