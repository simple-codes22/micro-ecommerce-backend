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

    def retrieve(self, request, product_name=None, product_id=None,):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, product_id=product_id)
        serializer = ProductSerializers(product)
        return Response(serializer.data)
    # def create(self, request, )

class ProductListSearch(ViewSet):
    renderer_classes = [JSONRenderer]
    
    def retrieve(self, request, product_name=None):
        queryset = Product.objects.filter(name__icontains=product_name)
        serializer = ProductSerializers(queryset, many=True)
        return Response(serializer.data)


class UserListViewSet(ViewSet):
    renderer_classes = [JSONRenderer]
    User = get_user_model()
    def list(self, request):
        queryset = self.User.objects.all()
        serializer = [user.username for user in queryset]
        return Response(serializer)

    def retrieve(self, request, email=None, password=None):
        queryset = self.User.objects.all()
        user = get_object_or_404(queryset, email=email)
        try:
            if user.check_password(password):
                serializer = UserSerializer(user)
                return Response(serializer.data)
        except Exception:
            return print("Did Not Work: ", Exception)
        serializer = UserSerializer(user)
        return Response(serializer.data)
        

class ProductImageListViewSet(ViewSet):
    renderer_classes = [JSONRenderer]
    def list(self, request):
        queryset = ProductImage.objects.all()
        serializer = ProductImageSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, product_id=None):
        queryset = ProductImage.objects.filter(product__id=product_id)
        serializer = ProductImageSerializer(queryset)
        return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     return


class OrderListViewSet(ViewSet):
    renderer_classes = [JSONRenderer]
    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, product_id=None):
        queryset = Order.objects.filter(product_ordered__product_id= product_id)
        serializer = OrderSerializer(queryset)
        return Response(serializer.data)

class ReviewListViewSet(ViewSet):
    renderer_classes = [JSONRenderer]
    def list(self, request):
        queryset = Review.objects.all()
        # serializer = ReviewSerializer(queryset)
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, product_id=None):
        queryset = Review.objects.filter(product_reviewed__product_id=product_id)
        serializer = ReviewSerializer(queryset)
        return Response(serializer.data)
    
