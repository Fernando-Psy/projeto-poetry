import pytest
from decimal import Decimal

from order.factories import OrderFactory, OrderItemFactory
from product.factories import ProductFactory
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_create_order_with_items():
    product = ProductFactory(price=Decimal("50.00"))
    order = OrderFactory()
    item = OrderItemFactory(order=order, product=product)

    client = APIClient()
    response = client.get(f"/api/orders/{order.id}/")
    assert order.items.count() == 1
    assert item.price == Decimal("50.00")
