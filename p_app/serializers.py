from rest_framework import serializers
from .models import (
    PizzaBase,
    Cheese,
    Topping,
    Pizza,
    PizzaOrder,
)


class PizzaBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaBase
        fields = ('id', 'name', 'price')


class CheeseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cheese
        fields = ('id', 'name', 'price')


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ('id', 'name', 'price')


class PizzaSerializer(serializers.ModelSerializer):
    base = PizzaBaseSerializer()
    cheese = CheeseSerializer()
    toppings = ToppingSerializer(many=True)

    class Meta:
        model = Pizza
        fields = ('id', 'base', 'cheese', 'toppings')


class PizzaOrderSerializer(serializers.ModelSerializer):
    pizzas = PizzaSerializer(many=True)  # Serialize multiple pizzas

    class Meta:
        model = PizzaOrder
        fields = ('id', 'pizzas', 'status')
