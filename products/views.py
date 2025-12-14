from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Product.DoesNotExist:
            return Response(
                {"error": "Producto no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
