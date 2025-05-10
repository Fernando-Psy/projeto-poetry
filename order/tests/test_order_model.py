import pytest
from decimal import Decimal

from order.factories import OrderFactory, OrderItemFactory
from product.factories import ProductFactory

@pytest.mark.django_db
def test_create_order_with_items():
    # Garantir que product tenha preço definido
    product = ProductFactory(price=Decimal('50.00'))
    order = OrderFactory()
    item = OrderItemFactory(order=order, product=product)

    assert order.items.count() == 1
    assert item.price == Decimal('50.00')  # Comparação precisa com Decimal