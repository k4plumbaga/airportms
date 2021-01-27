from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('airports', views.airport_list, name="airport_list"),
    path('airport/<str:pk>/flights', views.flight_list, name="flight_list"),
    path('allflights/', views.all_flights, name="all_flights"),
    path('allcustomers/', views.all_customers, name="all_customers"),
    path('flights/<int:id>/seats', views.seats, name="seats"),
    path('customers/<int:passport_number><str:country>/information', views.customers, name="customers"),
]
