from django.db import models


class PizzaBase(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6,
                                decimal_places=2)


class Cheese(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6,
                                decimal_places=2)


class Topping(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6,
                                decimal_places=2)


class Pizza(models.Model):
    base = models.ForeignKey(PizzaBase, on_delete=models.CASCADE)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)


class PizzaOrder(models.Model):
    pizzas = models.ManyToManyField(Pizza)
    status = models.CharField(max_length=100, default='Placed')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

