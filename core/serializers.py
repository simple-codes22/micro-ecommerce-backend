from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model


# Serializer for the Product model
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"  # Include all fields in the serialized representation


# Serializer for the ProductImage model
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"  # Include all fields in the serialized representation


# Serializer for the User model (custom user model)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # Get the custom user model
        fields = "__all__"  # Include all fields in the serialized representation


# Serializer for the Order model
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"  # Include all fields in the serialized representation

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"  # Include all fields in the serialized representation