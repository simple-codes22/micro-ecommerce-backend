from django.shortcuts import render
from rest_framework import mixins
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework import generics
from .models import *
from .serializers import *
from django.contrib.auth import get_user_model
from django.urls import reverse



def main_view(request, *args, **kwargs):
    return render(request, "backend-home.html", {})

class ProductList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    renderer_classes = [JSONRenderer]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ProductDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class ProductImageList(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class ProductImageDetail(
        mixins.RetrieveModelMixin,
        mixins.DestroyModelMixin,
        generics.GenericAPIView
    ):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class UserList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer

    renderer_classes = [JSONRenderer]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UserDetail(
        mixins.RetrieveModelMixin, 
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.GenericAPIView
    ):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class OrderList(
        mixins.ListModelMixin,
        generics.GenericAPIView, mixins.CreateModelMixin,
    ):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class OrderDetails(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.GenericAPIView
    ):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

