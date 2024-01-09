from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['customer_id'] = f"{user.customer_id}"
        token['email'] = user.email
        # token['cart'] = list(user.cart)
        token['date_joined'] = f"{user.date_joined}"

        return token

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
        extra_kwargs = {"password": {"write_only": True}}


# Serializer for the Order model
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"  # Include all fields in the serialized representation


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"  # Include all fields in the serialized representation
