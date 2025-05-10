from rest_framework import viewsets
from product.models import Product
from product.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet para visualizar, criar, editar e deletar produtos.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
