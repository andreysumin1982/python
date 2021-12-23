#--
from django.shortcuts import render
from .Classes import parsing_weather # Импортируем parsing_weather из Classes
from .Classes import connect_to_db
#--
import requests
from datetime import datetime
from django.http import JsonResponse

# Create your views here.
def index(request):
    '''Парсинг погоды'''
    if (request.method == 'GET'):
        context = parsing_weather.getData() # Метод getData() из модуля parsing_weather
        db = connect_to_db.connectDB()
        print(db)

        return render(request, 'weatherParser/weatherParser.html', context) # Вызвращает html
    elif (request.method == 'POST'):
        context = parsing_weather.getData()  # Метод getData() из модуля parsing_weather
        return JsonResponse(context) # Вызвращает json
#---
