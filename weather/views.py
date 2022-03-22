from django.shortcuts import render
import requests

def index(request):
    context={}
    url = 'https://api.weather.gov/gridpoints/TOP/31,80/forecast'

    city = 'Las Vegas'

    city_weather = requests.get(url).json() 
    context['data']=city_weather
    
    return render(request, 'index.html',context) 