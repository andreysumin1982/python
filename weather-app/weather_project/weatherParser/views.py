#--
from django.http import HttpResponse
from django.shortcuts import render
from .Classes import parsing_weather # Импортируем parsing_weather из Classes
from .Classes import sql_request
#--
from django.http import JsonResponse

# Create your views here.
def index(request):
    '''ф-ция  парсит погодные данные и выводит в формате HTML'''
    if (request.method == 'GET'):
        #tableName = ['city', 'osadki', 'image', 'summary'] # Список таблиц в базе
        context = parsing_weather.getData()  # Метод getData() из модуля parsing_weather
        return render(request, 'weatherParser/weatherParser.html', context) # Вызвращает html
#---
def getJson(request):
    if (request.method == 'GET'):
        context = parsing_weather.getData()  # Метод getData() из модуля parsing_weather
        return JsonResponse(context)  # Вызвращает json
#---
def showSummaryDate(request, str1, str2):
    if (request.method == 'GET'):
        summary = sql_request.getSummaryDate(str1, str2)
        #return HttpResponse(f"<h1>Работает</h1>{str1}{str2}</p>")
    return JsonResponse(summary)  # Вызвращает json
#---
def addData(request):
    '''Ф-ция вызывает хранимые процедуры из модуля sql_request'''
    if (request.method == 'GET'):
        context = parsing_weather.getData()  # Метод getData() из модуля parsing_weather, получаем словарь
        #
        # Заполняем таблицу city
        sql_request.insertDataCity(context['name'])

        # Заполняем таблицу image
        sql_request.insertDataImage(context['icon_name'], 'png', 'data')

        # Заполняем таблицу osadki
        sql_request.insertDataOsadki(context['description'], sql_request.showID('city'), sql_request.showID('image'))

        # Заполняем таблицу summary
        sql_request.insertDataSummary(sql_request.showID('city'), float(context['temp']), float(context['feels_like']), context['wind'], context['humidity'], sql_request.getDate())

    #return JsonResponse(context)
    return HttpResponse('Погодные данные добавлены в БД.')
#---
def delTable(request):
    '''ф-ция  удаление записей из таблиц'''
    if (request.method == 'GET'):
        sql_request.deleteDataSummary()
        sql_request.deleteDataOsadki()
        sql_request.deleteDataImage()
        sql_request.deleteDataCity()
    return HttpResponse('Данные из всех таблиц удалены.')
#---