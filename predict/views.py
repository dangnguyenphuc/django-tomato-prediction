from django.shortcuts import render, HttpResponse
from converted_keras import run
from django.http import JsonResponse
# Create your views here.
def home(request):
    return JsonResponse({
        "result": run.get_plant_health()
    })
