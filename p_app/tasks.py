from celery import shared_task
from django.utils import timezone
from .models import PizzaOrder
from logger import setup_logger


log = setup_logger()


@shared_task
def track_all_order_status():
    orders = PizzaOrder.objects.filter(status="Placed").all()
    log.info("Successfully fetched the all pizza orders")
    for order in orders:
        now = timezone.now()

        if now - order.created_at <= timezone.timedelta(minutes=1):
            log.info("Order status is Accepted.")
            status = 'Accepted'
        elif now - order.created_at <= timezone.timedelta(minutes=2):
            status = 'Preparing'
            log.info("Order status is Preparing.")
        elif now - order.created_at <= timezone.timedelta(minutes=5):
            status = 'Dispatched'
            log.info("Order status is Dispatched.")
        else:
            status = 'Delivered'
            log.info("Order status is Delivered.")

        order.status = status
        order.save()

    log.info("Successfully updated the statuses of all orders.")


@shared_task
def sample_task():
    print("cron job is working")
