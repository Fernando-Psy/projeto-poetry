# product/factories.py

import factory
from product.models import Product, Category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f"categoria-{n}")
    description = factory.Faker("sentence")


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("sentence", nb_words=4)
    description = factory.Faker("text")
    price = factory.Faker("pydecimal", left_digits=3, right_digits=2, positive=True)
    category = factory.SubFactory(CategoryFactory)