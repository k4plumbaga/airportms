from django.shortcuts import render, get_object_or_404
from .models import Airport,Flight,Flight_Leg,Seat,Customer

def airport_list(request):
    airports = Airport.objects.order_by('name')
    return render(request, 'mainapp/airport_list.html', {'airports':airports})

def airport_detail(request, pk):
    airport = get_object_or_404(Airport, pk = pk)
    flight_legs = Flight_Leg.objects.all()
    return render(request, 'mainapp/airport_detail.html', {'airport' : airport, 'flight_legs':flight_legs})

def flight_list(request, pk):
    airport = get_object_or_404(Airport, pk = pk)
    flight = Flight.objects.all()
    flight_legs = Flight_Leg.objects.all()
    return render(request, 'mainapp/flight_list.html', {'flight' : flight, 'airport' : airport, 'flight_legs':flight_legs})
