from rest_framework import viewsets
from order.models import Order
from order.serializers.order_serializer import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related("items__product").all()
    serializer_class = OrderSerializer
