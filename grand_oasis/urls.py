
from django.urls import path
from grand_oasis import views

urlpatterns = [
    path('', views.index, name="index"),
    path('rooms/', views.rooms, name="rooms"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
]
