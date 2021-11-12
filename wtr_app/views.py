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
        source = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=meteric&appid={api_key}').read()
        
        list_of_data = json.loads(source)
        data = {
            'country_code',
            'coordinate',
            'temp',
            'pressure',
            'humidity',
            'main',
            'description',
            'icon',
        }