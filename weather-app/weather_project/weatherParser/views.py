#--
from django.shortcuts import render
from .Classes import parsing_weather # Импортируем parsing_weather из Classes
from .Classes import sql_request
#--
from django.http import JsonResponse

# Create your views here.
def index(request):
    '''ф-ция вызывае парсинг погоды и выводит в консоль содержимое таблиц БД'''
    if (request.method == 'GET'):
        tableName = ['city', 'osadki', 'image', 'summary'] # Список таблиц в базе
        context = parsing_weather.getData()  # Метод getData() из модуля parsing_weather
        #
        for name in tableName: # Бежим по таблицам
            pass
            #print(sql_request.showTable(name)) # смотрим (вызываем sql_request.showTable() и передаем name)
            #
        print(sql_request.showID('city'))
        return render(request, 'weatherParser/weatherParser.html', context) # Вызвращает html
    #elif (request.method == 'POST'):
    #    context = parsing_weather.getData()  # Метод getData() из модуля parsing_weather
    #    return JsonResponse(context) # Вызвращает json
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
        sql_request.insertDataSummary(sql_request.showID('city'), float(context['temp']), float(context['feels_like']), int(context['wind']), int(context['humidity']))

    return JsonResponse(context)
#---
def delTable(request):
    '''ф-ция вызывает хранимую процедуру удаление записей из табдицы'''
    print(request)
    if (request.method == 'GET'):
        context = parsing_weather.getData()  # Метод getData() из модуля parsing_weather, получаем словарь
        sql_request.getFetchall(f"exec delTable 'summary'")
        sql_request.getFetchall(f"exec delTable 'osadki'")
        sql_request.getFetchall(f"exec delTable 'image'")
        sql_request.getFetchall(f"exec delTable 'city'")
    return JsonResponse(context)