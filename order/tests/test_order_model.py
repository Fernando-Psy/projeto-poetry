from decimal import Decimal

from order.models.order import Order
from rest_framework.test import APIClient


def test_create_order_with_items():
    class Product:
        def __init__(self):
            self.price = Decimal("50.00")
    product = Product()
    order = Order.objects.create()
    item = order.items.create(product=product, price=product.price, quantity=1)

    client = APIClient()
    response = client.get(f"/api/orders/{order.id}/")
    assert order.items.count() == 1
    assert item.price == Decimal("50.00")
