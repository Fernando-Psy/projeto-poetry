from rest_framework import serializers
from order.models import Order, OrderItem
from product.serializers.product_serializer import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity", "price", "total_price"]

    def get_total_price(self, obj):
        return obj.quantity * obj.product.price


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "customer_name", "created_at", "items"]
