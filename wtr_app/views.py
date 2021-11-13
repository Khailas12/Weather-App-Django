from django.conf.urls import url
from django.shortcuts import render
import urllib.request
import json
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv('WEATHER_API_KEY')


def index(request, *args, **kwargs):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}').read()
        
        list_of_data = json.loads(source)
        context = {
            'country_code': str(list_of_data['sys']['country']),
            'coordinate': str(list_of_data['coord']['lon']) + ', ' + str(list_of_data['coord']['lat']),
            'temp': str(list_of_data['main']['temp']) + ' °C',
            'pressure': str(list_of_data['main']['pressure']),
            'humidity': str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(context)
        
    else: 
        context = {}
    
    return render(request, 'index.html', context)