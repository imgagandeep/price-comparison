# Related third-party imports
from django.urls import path

# Local application/library specific imports
from apps.product.views import ProductsAPIViewSet

urlpatterns = [path("products/", ProductsAPIViewSet.as_view(), name="products")]
