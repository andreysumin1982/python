#--
from django.shortcuts import render
from .Classes import parsing_weather # Импортируем parsing_weather из Classes
from .Classes import connect_to_db
from .Classes import sql_request
#--
import requests
from datetime import datetime
from django.http import JsonResponse

# Create your views here.
def index(request):
    '''Парсинг погоды'''
    if (request.method == 'GET'):
        tableName = ['city', 'osadki', 'image', 'summary'] # Список таблиц в базе
        #
        for name in tableName: # Бежим по таблицам
            context = parsing_weather.getData() # Метод getData() из модуля parsing_weather
            db = connect_to_db.connectDB()
            data = db.execute(sql_request.showTable(name))
            print(data.fetchall())
        db.close()

        return render(request, 'weatherParser/weatherParser.html', context) # Вызвращает html
    elif (request.method == 'POST'):
        context = parsing_weather.getData()  # Метод getData() из модуля parsing_weather
        return JsonResponse(context) # Вызвращает json
#---
def addDate(request):
    '''Ф-ция вызывает хранимые процедуры из модуля sql_request'''
    if (request.method == 'GET'):
        context = parsing_weather.getData()  # Метод getData() из модуля parsing_weather, получаем словарь
        #
        db = connect_to_db.connectDB()
        # Заполняем таблицу city
        city = db.execute(sql_request.insertDataCity(context['name']))
        show = db.execute(sql_request.showTable('city'))
        print(show.fetchall())
        db.close()
    return JsonResponse(context)