from django.urls import path, include
from .views import *  # Import views from your app
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# Define the app name for namespacing
app_name = "core"

# Define URL patterns
urlpatterns = [
    # Default view for the root URL
    path("", main_view, name="ui-view"),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("product/", ProductListViewset.as_view({'get': 'list'}), name="product-list"),

    path("search/<str:product_name>", ProductListSearch.as_view({'get': 'retrieve'}), name="search-list"),

    path("product/<slug:product_id>", ProductListViewset.as_view({'get': 'retrieve'}), name="product-detail"),

    path("user/", UserListViewSet.as_view({"get": "list"}), name="user-list"),

    path("user/<str:email>/<str:password>", UserListViewSet.as_view({'get': 'retrieve'}), name="user-detail"),

    path("order/", OrderListViewSet.as_view({'get': 'list'}), name="order-list"),

    path("order/<slug:product_id>", OrderListViewSet.as_view({"get": "retrieve"}), name="order-details"),

    path("review/", ReviewListViewSet.as_view({'get': 'list'}), name="review-list"),

    path("review/<slug:product_id>", ReviewListViewSet.as_view({"get": 'retrieve'}), name="review-details"),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Serve media files during development (DEBUG mode)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
