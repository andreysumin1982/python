#-------------------------------------------------
from .connect_to_db import connectDB
from .connect_to_db import getFetchall
#-------------------------------------------------
def showTable(tableName):
    '''Смотрим содержимое таблицы'''
    result = getFetchall(f'exec showTable "{tableName}"')
    return result # Резельтат запроса - [(),] список
#
def showID(tablename):
    '''Ф-ция возвращает id'''
    #print('*', tablename)
    #print(f'SELECT max(id) from {tablename}')
    result = getFetchall(f'SELECT max(id) from {tablename}')
    print(result)
    return int(result[0][0]) # число
#
#-------------------------------------------------
'''Вызываем хранимые процедуры.'''
#-------------------------------------------------

def insertDataCity(cityName):
    '''Заносим полученные данные в таблицу city'''
    getFetchall(f"exec addCity '{cityName}'")
#
def insertDataImage(name, expansion, data):
    '''Заносим полученные данные в таблицу image'''
    getFetchall(f"exec addImage '{name}', '{expansion}', '{data}'")
#
def insertDataOsadki(description, id_city, id_image):
    '''Заносим полученные данные в таблицу osadki'''
    getFetchall(f"exec addOsadki '{description}', {id_city}, {id_image}")
#
def insertDataSummary(id_city, temperature, feels_like, wind, humidity):
    '''Заносим полученные данные в таблицу summary'''
    getFetchall(f"exec addSummary '{id_city}', '{temperature}', '{feels_like}', '{wind}', '{humidity}'")
#
