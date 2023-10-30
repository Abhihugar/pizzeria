from django.urls import path
from .views import (
    PizzaOrderCreateAPIView,
    PizzaInventory,
    PizzaOrderAPIView,
)

urlpatterns = [
    path('order/create/', PizzaOrderCreateAPIView.as_view(),
         name='create-pizza-order'),
    path('add/pizza-inventory/', PizzaInventory.as_view(), name='pizza'
                                                                '-inventory'),
    path('retrieve/pizza-inventory/items/', PizzaInventory.as_view(),
         name='pizza-inventory-items'),
    path('orders/', PizzaOrderAPIView.as_view(), name='pizza-order-list'),
    path('orders/<int:order_id>/', PizzaOrderAPIView.as_view(), name='pizza-order-detail'),
]

