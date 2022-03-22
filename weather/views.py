from django.shortcuts import render
import requests

def index(request):
    context={}
    url = 'https://api.weather.gov/gridpoints/TOP/31,80/forecast'

    city = 'Las Vegas'

    city_weather = requests.get(url).json()
    weather = {
        'city' : city,
        'temperature' : city_weather['properties']['periods'][0]['temperature'],
        'format': city_weather['properties']['periods'][0]['temperatureUnit'],
        'windspeed': city_weather['properties']['periods'][0]['windSpeed'],
        'direction': city_weather['properties']['periods'][0]['windDirection'],
        'description': city_weather['properties']['periods'][0]['detailedForecast'],
    }
    context['data']=weather
    
    return render(request, 'index.html',context) 