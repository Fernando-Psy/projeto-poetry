from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # ou liste os campos explicitamente: ['id', 'name', 'price', 'category', ...]