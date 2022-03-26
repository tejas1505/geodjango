#https://www.digitalocean.com/community/tutorials/how-to-build-a-weather-app-in-django

from django.shortcuts import render
import requests
from .models import city

def index(request):
    context={}
    cities=city.objects.all()
    weatherlist=[]
    for data in cities:
        url = 'https://api.weather.gov/points/'+ data.latitude +','+ data.longitude

        latlong = requests.get(url).json()
        url2=latlong["properties"]["forecast"]
        city_weather = requests.get(url2).json()
        weather = {
            'city' : data.name,
            'temperature' : city_weather['properties']['periods'][0]['temperature'],
            'format': city_weather['properties']['periods'][0]['temperatureUnit'],
            'windspeed': city_weather['properties']['periods'][0]['windSpeed'],
            'direction': city_weather['properties']['periods'][0]['windDirection'],
            'description': city_weather['properties']['periods'][0]['detailedForecast'],
            'latitude': data.latitude,
            'longitude': data.longitude,
        }
        weatherlist.append(weather)
    context['data']=weatherlist
    context['length']=len(weatherlist)
    
    return render(request, 'index.html',context) 
