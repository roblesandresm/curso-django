"""Platzigram views"""
from django.http import HttpResponse

# utilities
from datetime import datetime
import json 

def root(request):
    return HttpResponse("ESTAS EN EL HOME")

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M')
    return HttpResponse(
        f'Hello world. current server time is {now}'
    )

def sort_integers(request):
    numbers = request.GET["numbers"]
    numbers = [int(i) for i in numbers.split(",")]
    sorted_int = sorted(numbers)
    data = {
        "status": "ok",
        "numbers": sorted_int,
        "message": "Intagers sorted successfully."
    }
    
    return HttpResponse(
        json.dumps(data), 
        content_type="application/json"
    )

def say_hi(request, name, age):
    if age < 12:
        message = f"lo siento {name} No tienes la edad para ingresar"
    else:
        message = f"Adelante {name} Puedes disfrutar de todo el contenido"

    return HttpResponse(message)