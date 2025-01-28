from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image_url']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'product_name', 'ingredients', 'difficulty_level', 'time_required', 
                  'price_inr', 'egg_or_eggless', 'quantity', 'description', 'reviews', 'ratings', 'created_date']