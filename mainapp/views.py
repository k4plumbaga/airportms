from django.shortcuts import render, get_object_or_404
from .models import Airport,Flight,Flight_Leg,Seat,Customer,Leg_Instance,FFC
import datetime
from django.utils import timezone
from django.db.models.functions import TruncMonth
from django.db.models import Count

def all_customers(request):
    customers = Customer.objects.all()
    return render(request, 'mainapp/all_customers.html', {'customers':customers})

def all_flights(request):
    leg_instances = Leg_Instance.objects.all()
    return render(request, 'mainapp/all_flights.html', {'leg_instances':leg_instances})

def home(request):
    airports = Airport.objects.all()
    leg_instances = Leg_Instance.objects.all()
    most_airports=(Leg_Instance.objects.values('departure_airport_code').annotate(dcount=Count('departure_airport_code')).order_by('-dcount'))
    most_airports_names = [i['departure_airport_code'] for i in most_airports]
    most_airports_counts = [i['dcount'] for i in most_airports]
    months_counts = []
    for i in range(12):
        months_counts.append(Leg_Instance.objects.filter(date__month = str(i+1)).count())
    customers = Customer.objects.all()
    return render(request, 'mainapp/home.html', {'airports':airports, 'leg_instances':leg_instances, 'customers':customers, 'months':months_counts, 'most_airports_counts':most_airports_counts, 'most_airports_names':most_airports_names, })

def airport_list(request):
    airports = Airport.objects.order_by('name')
    return render(request, 'mainapp/airport_list.html', {'airports':airports})

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
