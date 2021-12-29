#-------------------------------------------------
from .connect_to_db import connectDB
from .connect_to_db import getFetchall
#-------------------------------------------------
def showTable(tableName):
    '''Смотрим содержимое таблицы'''
    result = getFetchall(f'select * from {tableName}')
    return result # Резельтат запроса - [(),] список
#
def showID(tablename):
    '''Ф-ция возвращает id'''
    result = getFetchall(f'SELECT max(id) from {tablename}')
    return int(result[0][0]) # число
#-------------------------------------------------
'''Хранимые процедуры'''
#-------------------------------------------------

def insertDataCity(cityName):
    '''Заносим полученные данные в таблицу city'''
    db = connectDB()
    db.execute(f"insert into city (name) values ('{cityName}')")
    db.commit()
    db.close()
#
def insertDataImage(name, expansion):
    '''Заносим полученные данные в таблицу image'''
    db = connectDB()
    db.execute(f"insert into image (name, expansion) values ('{name}', '{expansion}')")
    db.commit()
    db.close()
#
def insertDataOsadki(description, id_city, id_image):
    '''Заносим полученные данные в таблицу osadki'''
    db = connectDB()
    db.execute(f"insert into osadki (description, id_city, id_image) values ('{description}', {id_city}, {id_image})")
    db.commit()
    db.close()
#
def insertDataSummary(id_city, temperature, feels_like, wind, humidity):
    '''Заносим полученные данные в таблицу summary'''
    db = connectDB()
    db.execute(f"insert into summary (id_city, temperature, feels_like, wind, humidity) values ('{id_city}', '{temperature}', '{feels_like}', '{wind}', '{humidity}')")
    db.commit()
    db.close()
#
