
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('grand_oasis.urls')),
    path('django-admin/', admin.site.urls),
]
