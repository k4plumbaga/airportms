from django.contrib import admin

from .models import Airport,Flight,Flight_Leg,Airplane,Leg_Instance,Fare,Company,Airplane_Type,FFC,Customer,Seat,Airline,Airplane_Manufacturer
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Flight_Leg)
admin.site.register(Airplane)
admin.site.register(Leg_Instance)
admin.site.register(Fare)
admin.site.register(Company)
admin.site.register(Airplane_Type)
admin.site.register(FFC)
admin.site.register(Customer)
admin.site.register(Seat)
admin.site.register(Airline)
admin.site.register(Airplane_Manufacturer)
# Register your models here.
