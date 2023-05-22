from django.contrib import admin
from .models import *

admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(Contact)

admin.site.register(ServiceType)
admin.site.register(ExtraService)
admin.site.register(ServiceDate)