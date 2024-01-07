from django.urls import path, include
from .views import *  # Import views from your app
from django.conf.urls.static import static
from django.conf import settings

# Define the app name for namespacing
app_name = "core"

# Define URL patterns
urlpatterns = [
    # Default view for the root URL
    path("", main_view, name="ui-view"),
    # User-related URLs
    path("user/", UserList.as_view(), name="user-list"),  # List of users
    path(
        "user/create", UserCreate.as_view(), name="user-create"
    ),  # User detail by primary key
    path("user/<str:email>", UserDetail.as_view(), name="user-detail"),
    # Product-related URLs
    path("product/", ProductList.as_view(), name="product-list"),  # List of products
    path(
        "product/<str:pk>", ProductDetail.as_view(), name="product-detail"
    ),  # Product detail by primary key
    # Product image-related URLs
    path(
        "product-image/", ProductImageList.as_view(), name="product-image(s)"
    ),  # List of product images
    path(
        "product-image/<str:pk>",
        ProductImageDetail.as_view(),
        name="product-image-detail",
    ),  # Product image detail by primary key
    # Order-related URLs
    path("order/", OrderList.as_view(), name="order-list"),  # List of orders
    path(
        "order/<str:pk>", OrderDetails.as_view(), name="order-details"
    ),  # Order detail by primary key
    path("review/", ReviewList.as_view(), name="review-list"),  # List of reviews
    path(
        "review/<str:pk>", ReviewDetails.as_view(), name="review-details"
    ),  # Review detail by primary key
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Serve media files during development (DEBUG mode)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
