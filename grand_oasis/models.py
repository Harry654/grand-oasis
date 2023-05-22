from django.contrib.auth.models import User
from django.db import models
    
class Room(models.Model):
    CATEGORY = (('Junior Suite', 'Junior Suite'), ('Executive Suite',
                'Executive Suite'), ('Super Deluxe', 'Super Deluxe'),)
    category = models.CharField(max_length=120, null=True, choices=CATEGORY)
    room_number = models.IntegerField()
    floor_number = models.IntegerField()
    price_per_night = models.IntegerField()
    description = models.CharField(max_length=500, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.room_number} {self.category}"
    
class Reservation(models.Model):
    user= models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
    room= models.ForeignKey(Room, on_delete=models.CASCADE)
    date_booked = models.DateTimeField(auto_now_add=True)
    checkin = models.DateField()
    checkout = models.DateField()
    duration = models.CharField(max_length=20, null=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, default=0)

    def __str__(self):
        return f"Room {self.room.room_number} on floor {self.room.floor_number} booked by {self.user.username} for {self.duration} days"

class ServiceType(models.Model):
    SERVICE_CHOICES = (
        ('Airport Pick-up', 'pick_up'),
        ('Airport Drop-off', 'drop_off'),
        ('Food & Restaurant', 'food'),
        ('Spa & Fitness', 'spa'),
        ('Sports & Gaming', 'sports'),
        ('Event & Party', 'party'),
        ('GYM & Yoga', 'gym'),
    )
    type = models.CharField(max_length=100, choices=SERVICE_CHOICES, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.type} -- ${self.price}"
        
class ExtraService(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='extra_services')
    service = models.ForeignKey(ServiceType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.reservation.user.username} of Reservation {self.reservation.id} demands {self.service.type}"

class ServiceDate(models.Model):
    extra_service = models.ForeignKey(ExtraService, on_delete=models.CASCADE)
    service_date_time = models.DateTimeField()
    
    def __str__(self):
        return f"{self.extra_service} scheduled for {self.service_date_time}"
    
class Contact(models.Model):
    msg_sender= models.ForeignKey(User, null=True, on_delete= models.SET_NULL, related_name="msg_sender")
    msg_receiver= models.ForeignKey(User, on_delete=models.CASCADE, related_name="msg_receiver")
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=500)
    date_sent = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"From {'admin' if self.msg_sender.is_staff else self.msg_sender} to {'admin' if self.msg_receiver.is_staff else self.msg_receiver}"
    

# print(len(ExtraService.objects.all()))
# reservation = Reservation.objects.get(id=23)
# # print(reservation.total_price)
# extra_service = ExtraService.objects.create(reservation=reservation, type='Spa & Fitness', price=20.00)

# # Update the reservation total price
# reservation.update_total_price()