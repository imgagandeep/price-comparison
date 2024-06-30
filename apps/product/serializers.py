# Related third-party imports
from rest_framework.serializers import ModelSerializer

# Local application/library specific imports
from apps.product.models import Product


class MainProductsSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CreateProductSerializer(MainProductsSerializer):

    class Meta(MainProductsSerializer.Meta):
        fields = ["name", "price", "retailer_name"]
        extra_kwargs = {"id": {"read_only": True}}


class ListProductSerializer(MainProductsSerializer):

    class Meta(MainProductsSerializer.Meta):
        fields = ["id", "name", "price", "retailer_name"]
