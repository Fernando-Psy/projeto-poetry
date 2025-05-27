from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated as IsAutenticated
from order.models import Order
from order.serializers.order_serializer import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related("items__product").all()
    serializer_class = OrderSerializer

    authentication_classes = [ BasicAuthentication, TokenAuthentication ]
    permission_classes = [IsAutenticated]
