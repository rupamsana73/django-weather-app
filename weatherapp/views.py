from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests

API_KEY = "3c0993f78cbd22fdde983556cd1d59a9"

# ---------- AUTH ----------
def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('weather')
        else:
            return render(request, "login.html", {"error": "Invalid login"})
    return render(request, "login.html")


def signup_view(request):
    if request.method == "POST":
        User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        return redirect('login')
    return redirect('login')


def logout_view(request):
    logout(request)
    return redirect('login')


# ---------- WEATHER PAGE ----------
@login_required(login_url='login')
def weather_home(request):
    return render(request, "weather.html")

@login_required(login_url='login')
def about_view(request):
    return render(request, "about.html")



@login_required(login_url='login')
def get_weather(request):
    city = request.GET.get("city", "")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return JsonResponse({"cod": "404", "message": "City not found"})

    return JsonResponse(response.json())

# ---------- FORECAST PAGE ----------
@login_required(login_url='login')
def get_forecast(request):
    city = request.GET.get("city", "")

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return JsonResponse({"cod": "404", "message": "Forecast not found"})

    return JsonResponse(response.json())
