from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from .models import ReservationModel

@receiver(pre_delete, sender=ReservationModel)
def set_room_availability(sender, instance, **kwargs):
    instance.room.is_available = True
    instance.room.save()

@receiver(pre_save, sender=ReservationModel)
def calculate_booking_total_price(sender, instance, **kwargs):
    room = instance.room
    checkin = instance.checkin
    checkout = instance.checkout
    nights = (checkout - checkin).days
    total_price = room.price_per_night * nights
    instance.total_price = total_price