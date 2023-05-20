from django.db import models
    
class RoomModel(models.Model):
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
    
class ReservationModel(models.Model):
    # client= models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
    room= models.ForeignKey(RoomModel, on_delete=models.CASCADE)
    date_booked = models.DateTimeField(auto_now_add=True)
    checkin = models.DateField()
    checkout = models.DateField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)


    def __str__(self):
        return f"Room {self.room.room_number} on floor {self.room.floor_number} booked by"