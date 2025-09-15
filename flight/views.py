from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import  Flight, Passenger


# Create your views here.
def index(request):
    flights = Flight.objects.all()
    return render(
        request, "flight/index.html", {"flights": flights} 
    )


def ind_flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(
        request,
        "flight/flight.html",
        {
            "flight": flight,
            "passengers": flight.passengers.all(),
            "no_passengers": Passenger.objects.exclude(flight=flight),
        },
    )


def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        passenger.flight.add(flight)  # many-to-many add
        return HttpResponseRedirect(reverse("flight", args=[flight_id]))
