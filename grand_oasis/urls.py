
from django.urls import path
from grand_oasis import views

urlpatterns = [
    path('', views.index, name="index"),
    path('rooms/', views.rooms, name="rooms"),
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name="login"),
    path('contact/', views.contact, name="contact"),
    path('admin/', views.admin, name="admin"),
    path('my-bookings/', views.myBookings, name="myBookings"),
]
