from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from logger import setup_logger
from .models import (
    PizzaOrder,
    Pizza,
    PizzaBase,
    Cheese,
    Topping,
)
from .serializers import (
    PizzaOrderSerializer,
    PizzaBaseSerializer,
    CheeseSerializer,
    ToppingSerializer,
)

log = setup_logger()


class PizzaOrderCreateAPIView(APIView):
    """
    API endpoint for creating pizza orders.

    Attributes:
        None

    Methods: post(request, *args, **kwargs): Handle POST requests to create
    pizza orders.
    """

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to create pizza orders.

        Args:
            request (Request): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns: Response: JSON response indicating the success or failure
        of the operation.
        """
        orders_data = request.data.get('orders',
                                       [])
        log.info("Started processing the Pizza order.")
        created_orders = []
        for order_data in orders_data:
            pizzas_data = order_data.get('pizzas', [])

            # Deserialize and create pizzas for the order
            pizzas = []
            for pizza_data in pizzas_data:
                base_id = pizza_data.get('base')
                cheese_id = pizza_data.get('cheese')
                toppings_ids = pizza_data.get('toppings', [])

                try:
                    base = PizzaBase.objects.get(pk=base_id)
                    cheese = Cheese.objects.get(pk=cheese_id)
                    toppings = Topping.objects.filter(pk__in=toppings_ids)

                    pizza = Pizza.objects.create(base=base, cheese=cheese)
                    pizza.toppings.set(toppings)
                    pizzas.append(pizza)
                except Exception as e:
                    log.info("Please check the or add the valid inventory "
                             f"item -> {e}.")
                    # Handle invalid IDs or other errors as needed
                    return Response(
                        {'error': 'Invalid pizza inventory.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )

            # Create the PizzaOrder instance
            pizza_order = PizzaOrder.objects.create()
            pizza_order.pizzas.set(pizzas)
            created_orders.append(pizza_order)

        serializer = PizzaOrderSerializer(created_orders, many=True)
        log.info("Successfully placed the pizza order at pizzeria.")
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PizzaOrderAPIView(APIView):
    """
    API endpoint for retrieving pizza orders.

    Attributes:
        None

    Methods:
        get(order_id=None, *args, **kwargs):
        Handle GET requests to retrieve pizza orders.
    """

    def get(self, order_id=None, *args, **kwargs):
        """
        Handle GET requests to retrieve pizza orders.

        optional): The ID of the specific pizza order to retrieve. *args:
        Additional positional arguments. **kwargs: Additional keyword
        arguments.

        Returns: Response: JSON response containing the pizza order data or
        an error message if the order is not found.
        """
        if order_id:
            try:
                order = PizzaOrder.objects.get(pk=order_id)
                serializer = PizzaOrderSerializer(order)
                return Response(serializer.data)
            except Exception as e:
                return Response(
                    {'error': 'Order not found'},
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            orders = PizzaOrder.objects.all()
            serializer = PizzaOrderSerializer(orders, many=True)
            return Response(serializer.data)


class PizzaInventory(APIView):
    """
    API endpoint for managing pizza inventory items.

    Attributes:
        None

    Methods: post(request, *args, **kwargs): Handle POST requests to add
    pizza inventory items.
    """

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to add pizza inventory items.

        Args:
            request (Request): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns: Response: JSON response indicating the success or failure
        of the operation.
        """
        pizza_base_serializer = PizzaBaseSerializer(
            data=request.data.get('pizza_base'))
        cheese_serializer = CheeseSerializer(data=request.data.get('cheese'))
        topping_serializer = ToppingSerializer(
            data=request.data.get('topping'))

        if (pizza_base_serializer.is_valid() and cheese_serializer.is_valid()
                and topping_serializer.is_valid()):
            pizza_base_serializer.save()
            cheese_serializer.save()
            topping_serializer.save()
            log.info("Successfully Added pizza inventory item.")
            return Response(
                {'message': 'Successfully Added pizza inventory items'},
                status=status.HTTP_201_CREATED)
        else:
            errors = {
                'pizza_base_errors': pizza_base_serializer.errors,
                'cheese_errors': cheese_serializer.errors,
                'topping_errors': topping_serializer.errors
            }
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, *args, **kwargs):
        """
        Handle GET requests to retrieve data from PizzaBase, Cheese,
        and Topping models.

        Args:
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns: Response: JSON response containing data from all models.
        """
        pizza_base_data = PizzaBaseSerializer(PizzaBase.objects.all(),
                                              many=True).data
        cheese_data = CheeseSerializer(Cheese.objects.all(), many=True).data
        topping_data = ToppingSerializer(Topping.objects.all(), many=True).data

        response_data = {
            'pizza_base': pizza_base_data,
            'cheese': cheese_data,
            'topping': topping_data
        }

        return Response(response_data, status=status.HTTP_200_OK)
