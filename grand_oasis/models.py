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


class ClientRegisterModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

class ClientLoginModel(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
