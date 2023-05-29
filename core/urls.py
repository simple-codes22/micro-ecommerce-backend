from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings


app_name='core'

urlpatterns = [
    # User List
    path('user/', UserList.as_view(), name="user-list"),
    path('user/<str:pk>/', UserDetail.as_view(), name="user-detail"),

    # Product data
    path('product/', ProductList.as_view(), name="product-list"),
    path('product/<str:pk>', ProductDetail.as_view(), name="product-detail"),
    
    # Order data
    path('order/', OrderList.as_view(), name="order-list"),
    path('order/<str:pk>', OrderDetails.as_view(), name="order-details"),
]
# For image files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)