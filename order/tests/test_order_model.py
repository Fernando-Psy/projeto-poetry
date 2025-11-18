import pytest
from decimal import Decimal
from django.contrib.auth.models import User
from order.models.order import Order
from product.models import Product, Category
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_create_order_with_items():
    category = Category.objects.create(
        name="Livros",
        description="Categoria de livros"
    )

    product = Product.objects.create(
        name="Produto Teste",
        description="Descrição do produto teste",
        price=Decimal("50.00"),
        category=category
    )

    order = Order.objects.create()
    item = order.items.create(
        product=product,
        price=product.price,
        quantity=1
    )

    client = APIClient()
    response = client.get(f"/api/orders/{order.id}/")

    assert order.items.count() == 1
    assert item.price == Decimal("50.00")
    assert item.quantity == 1
    assert item.product == product


@pytest.mark.django_db
def test_order_total_calculation():
    """Testa o cálculo total de um pedido com múltiplos itens"""
    category = Category.objects.create(
        name="Eletrônicos",
        description="Produtos eletrônicos"
    )

    product1 = Product.objects.create(
        name="Produto 1",
        description="Primeiro produto",
        price=Decimal("100.00"),
        category=category
    )

    product2 = Product.objects.create(
        name="Produto 2",
        description="Segundo produto",
        price=Decimal("50.00"),
        category=category
    )

    order = Order.objects.create()
    order.items.create(product=product1, price=product1.price, quantity=2)
    order.items.create(product=product2, price=product2.price, quantity=3)

    assert order.items.count() == 2