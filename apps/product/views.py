# Related third-party imports
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Local application/library specific imports
from loggers import logger
from apps.product.models import Product
from apps.product.serializers import CreateProductSerializer, ListProductSerializer


# Create your views here.
class ProductsAPIViewSet(APIView):
    queryset = Product.objects.all()

    def get(self, request):
        param = request.query_params.get("name")

        filters = {"is_deleted": False}
        if param:
            filters["name"] = param

        try:
            queryset = Product.objects.filter(**filters)

            data = {}
            products = []
            for i in queryset:
                if i.name in products:
                    data[i.name].append(
                        {"retailer": i.retailer_name, "price": float(i.price)}
                    )
                else:
                    data[i.name] = [
                        {"retailer": i.retailer_name, "price": float(i.price)}
                    ]
                    products.append(i.name)

            response = {
                "success": True,
                "message": "Products are retrieved successfully.",
                "data": data,
            }

            return Response(response, status=status.HTTP_200_OK)
        except Exception as error:
            logger.error(error)
            response = {
                "success": False,
                "message": "Products are not retrieved successfully.",
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        # prepare data
        prepared_data = {
            "name": request.data.get("name"),
            "price": request.data.get("price"),
            "retailer_name": request.data.get("retailer_name"),
        }

        try:
            serializer = CreateProductSerializer(data=prepared_data)
            serializer.is_valid(raise_exception=True)
            created_instances = serializer.save()

            response_serializer = ListProductSerializer(created_instances).data
            return Response(
                {
                    "success": True,
                    "message": "Product has been created successfully.",
                    "data": response_serializer,
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as error:
            logger.error(error)
            response = {
                "success": False,
                "message": "Product has not been created successfully.",
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
