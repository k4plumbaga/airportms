from django.shortcuts import render, get_object_or_404
from .models import Airport,Flight,Flight_Leg,Seat,Customer,Leg_Instance,FFC

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
    leg_instance = Leg_Instance.objects.all().order_by('date','departue_time')
    return render(request, 'mainapp/flight_list.html', {'flight' : flight, 'airport' : airport, 'leg_instance':leg_instance})

def seats(request, id):
    leg_instance = get_object_or_404(Leg_Instance, id = id)
    seats = Seat.objects.all().order_by('seat_number')
    customer = Customer.objects.all()
    return render(request, 'mainapp/flight_seats.html', {'leg_instance':leg_instance, 'seats':seats, 'customer':customer})

def customers(request, passport_number, country):
    customers = get_object_or_404(Customer, passport_number = passport_number, country = country)
    ffcs = FFC.objects.all()
    seats = Seat.objects.all()
    leg_instances = Leg_Instance.objects.all().order_by('date')
    return render(request, 'mainapp/customers.html', {'customers':customers, 'ffcs':ffcs, 'seats':seats, 'leg_instances':leg_instances})
