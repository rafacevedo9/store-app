# products/infrastructure/views.py

from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    """
    Endpoint que permite realizar operaciones CRUD sobre Productos.
    Métodos soportados automáticamente: GET, POST, PUT, DELETE.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer