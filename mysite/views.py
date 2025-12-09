from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def home(request):
    return render(request, 'homepage.html')

def jsonData(request):
    data = {
        'My Info In': 'JSON',
        'name': 'Suraj Mirajkar',
        'age': 39,
        'city': 'Pune',
        'state': 'Maharashtra',
        'postal_code': 411033,
        'country': 'India'
    }
    return JsonResponse(data)

def about(request):
    return render(request, 'about.html')

def htmlData(request):
    return HttpResponse("<h1>My Info In HTML:</h1> <p>Name: Suraj Mirajkar, Age: 39, City: Pune, State: Maharashtra, Postal Code: 411033, Country: India</p>")