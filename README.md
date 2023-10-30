# pizzeria
# To start the application 
    docker-compose up --build
# pizzeria Ordering System API Documentation
    Create Pizza Order
    
    Endpoint: POST /order/create/
    
    Description: Create a new pizza order with specified pizzas and their components (base, cheese, toppings).
    Retrieve Pizza Orders

    curl --location 'http://localhost:8000/pizza/order/create/' \
    --header 'Content-Type: application/json' \
    --data '{
        "orders": [
            {
                "pizzas": [
                    {"base": 1, "cheese": 1, "toppings": [2, 3]},
                    {"base": 2, "cheese": 2, "toppings": [4, 5, 6]}
                ]
            },
            {
                "pizzas": [
                    {"base": 1, "cheese": 2, "toppings": [3, 4]},
                    {"base": 3, "cheese": 1, "toppings": [5, 6, 7]}
                ]
            }
        ]
    }
    '
#
    Endpoint: GET /orders/
    
    Description: Retrieve a list of all pizza orders.
    Add Pizza Inventory Items
    
    # Get list of orders
    curl --location 'http://localhost:8000/pizza/orders/'

    # check order status
    curl --location 'http://localhost:8000/pizza/orders/1/'

#
    Endpoint: POST /add/pizza-inventory/
    
    Description: Add new pizza inventory items such as pizza base, cheese, and toppings.
    Retrieve Pizza Inventory Items

    curl --location 'http://localhost:8000/pizza/add/pizza-inventory/' \

    --header 'Content-Type: application/json' \
    --data '{
      "pizza_base": {
        "name": "Thin Crust",
        "price": "9.99"
      },
      "cheese": {
        "name": "Mozzarella",
        "price": "4.99"
      },
      "topping": {
        "name": "Pepperoni",
        "price": "2.50"
      }
    }
#
    Endpoint: GET /retrieve/pizza-inventory/items/
    
    Description: Retrieve data from PizzaBase, Cheese, and Topping models.

    curl --location 'http://localhost:8000/pizza/retrieve/pizza-inventory/items/'


# docker will handle the restart if django is not able to connect to db

# Env file
    DEFAULT_DATABASE_HOSTNAME=localhost
    DEFAULT_DATABASE_USER=abhishek
    DEFAULT_DATABASE_PASSWORD=ascend
    DEFAULT_DATABASE_PORT=3306
    DEFAULT_DATABASE_DB=pizzeria
