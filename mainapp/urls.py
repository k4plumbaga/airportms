from django.urls import path
from . import views
urlpatterns = [
    path('', views.airport_list, name="airport_list"),
    path('airport/<str:pk>/', views.airport_detail, name="airport_detail"),
    path('airport/<str:pk>/flights', views.flight_list, name="flight_list"),
    path('flights/<int:id>/seats', views.seats, name="seats"),
    path('customers/<int:passport_number><str:country>/information', views.customers, name="customers"),
]
