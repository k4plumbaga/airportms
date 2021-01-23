from django.urls import path
from . import views
urlpatterns = [
    path('', views.airport_list, name="airport_list"),
    #path('airport/<int:pk>/', views.airport_detail, name="airport_detail"),
    path('airport/<int:pk>/flights', views.flight_list, name="flight_list"),
]
