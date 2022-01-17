#-------------------------------------------------
#from .connect_to_db import connectDB
from .connect_to_db import getFetchall
from .connect_to_db import insertData
from .connect_to_db import deleteData
#-------------------------------------------------
def showTable(tableName):
    '''Смотрим содержимое таблицы'''
    result = getFetchall(f'exec showTable "{tableName}"')
    return result # Резельтат запроса - [(),] список
#
def showID(tablename):
    '''Ф-ция возвращает id'''
    result = getFetchall(f'SELECT max(id) from {tablename}')
    return int(result[0][0]) # число
#
def getSummaryDate(date1, date2):
    result = getFetchall(f'exec showSummaryDate "{date1}", "{date2}"')
    i = 0
    summary = {}
    for res in result:
        stroka = str(res)[1:-2]  # обрезаем лишние символы, пробелы.
        summary.update({f"{i}": f"{stroka}"});
        i += 1
    return summary
#
def getDate():
    '''Ф-ция возвр объект datetime'''
    result = getFetchall(f'exec getDate')
    return str(result[0][0])
#-------------------------------------------------
'''Вызываем хранимые процедуры.'''
#-------------------------------------------------

def insertDataCity(cityName):
    '''Заносим полученные данные в таблицу city'''
    insertData(f"exec addCity '{cityName}'")
#
def insertDataImage(name, expansion, data):
    '''Заносим полученные данные в таблицу image'''
    insertData(f"exec addImage '{name}', '{expansion}', '{data}'")
#
def insertDataOsadki(description, id_city, id_image):
    '''Заносим полученные данные в таблицу osadki'''
    insertData(f"exec addOsadki '{description}', {id_city}, {id_image}")
#
def insertDataSummary(id_city, temperature, feels_like, wind, humidity, date_time):
    '''Заносим полученные данные в таблицу summary'''
    insertData(f"exec addSummary '{id_city}', '{temperature}', '{feels_like}', '{wind}', '{humidity}', '{date_time}'")
#
def deleteDataCity():
    deleteData(f"exec delTable 'city'")
#
def deleteDataImage():
    deleteData(f"exec delTable 'image'")
#
def deleteDataOsadki():
    deleteData(f"exec delTable 'osadki'")
#
def deleteDataSummary():
    deleteData(f"exec delTable 'summary'")
#