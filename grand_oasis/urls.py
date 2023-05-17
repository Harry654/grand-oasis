
from django.urls import path
from grand_oasis import views

urlpatterns = [
    path('', views.index, name="index"),
]
