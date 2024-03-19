import logging
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Log, Order


@receiver(post_save, sender=Order)
def create_order(sender, **kwargs):
    instance = kwargs['instance']
    price = instance.price
    logging_message = f'Новый заказ с ценой {price}'
    Log.objects.create(text=logging_message)


