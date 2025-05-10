import factory
from order.models import Order, OrderItem
from product.factories import ProductFactory


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    customer_name = factory.Faker("name")


class OrderItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderItem

    order = factory.SubFactory(OrderFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = 1
