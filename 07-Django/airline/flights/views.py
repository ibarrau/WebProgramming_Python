from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Flight, Airport, Passanger
from django.urls import reverse

# Create your views here.
def index(request):
    context = {
        "flights": Flight.objects.all()
    }
    return render(request, "flights/index.html", context)

def flight(request, flight_id):
    try:
        flight=Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exists.")
    context = {
        "flight":flight,
        "passangers":flight.passangers.all(),
        "non_passangers": Passanger.objects.exclude(flights=flight).all()
    }
    return render(request, "flights/flight.html", context)

def book(request, flight_id):
    try:
        passanger_id = int(request.POST["passanger"])
        passanger = Passanger.objects.get(pk=passanger_id)
        flight = Flight.objects.get(pk=flight_id)
    except KeyError:
        return render(request, "flights/error.html", {"message": "No selection."})
    except Flight.DoesNotExist:
        return render(request, "Flights/error.html", {"message": "No Flight."})
    except Passanger.DoesNotExist:
        return render(request, "Flights/error.html", {"message": "No Passanger."})
    
    passanger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight", args=(flight_id,)))