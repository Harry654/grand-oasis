from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from .models import Reservation
from django.db.models import Sum

@receiver(pre_delete, sender=Reservation)
def set_room_availability(sender, instance, **kwargs):
    instance.room.is_available = True
    instance.room.save()

@receiver(pre_save, sender=Reservation)
def calculate_booking_duration(sender, instance, **kwargs):
    checkin = instance.checkin
    checkout = instance.checkout
    instance.duration = (checkout - checkin).days

@receiver(pre_save, sender=Reservation)
def calculate_booking_total_price(sender, instance, **kwargs):
    if not instance.total_price:
        room = instance.room
        checkin = instance.checkin
        checkout = instance.checkout
        nights = (checkout - checkin).days
        total_price = room.price_per_night * nights
        instance.total_price = instance.total_price + total_price
