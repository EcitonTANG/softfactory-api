from rest_framework import serializers

from .models import *


class MealItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealsItems
        fields = '__all__'


class CategoryItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryItems
        fields = '__all__'


class MealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = '__all__'
