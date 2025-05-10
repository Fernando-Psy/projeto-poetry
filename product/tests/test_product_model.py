from django.test import TestCase
from product.models import Category, Product


class ProductModelTest(TestCase):
    def setUp(self):
        # Cria uma categoria para usar nos testes
        self.category = Category.objects.create(
            name="Ficção Científica",
            description="Livros de ficção científica e fantasia",
        )

        # Cria um produto associado à categoria
        self.product = Product.objects.create(
            name="O Guia do Mochileiro das Galáxias",
            description="Uma clássica aventura espacial cheia de humor.",
            price=49.90,
            category=self.category,
        )

    def test_create_category(self):
        self.assertEqual(self.category.name, "Ficção Científica")
        self.assertEqual(str(self.category), "Ficção Científica")

    def test_create_product(self):
        self.assertEqual(self.product.name, "O Guia do Mochileiro das Galáxias")
        self.assertEqual(self.product.price, 49.90)
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(str(self.product), "O Guia do Mochileiro das Galáxias")
