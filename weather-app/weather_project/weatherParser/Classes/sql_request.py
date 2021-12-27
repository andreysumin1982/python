#
def showTable(tableName):
    '''Смотрим содержимое таблицы'''
    return f'select * from {tableName}'
#
'''Хранимые процедуры SQL'''
#
def insertDataCity(cityName):
    '''Заносим полученные данные в таблицу city'''
    return f"insert into city (name) values ('{cityName}')"
#
def insertDataOsadki(description, id_city, id_image):
    '''Заносим полученные данные в таблицу osadki'''
    return f"insert into osadki (description, id_city, id_image) values ('{description}', '{id_city}', '{id_image}')"
#
def insertDataImage(name, expansion, data):
    '''Заносим полученные данные в таблицу city'''
    return f"insert into image (name, expansion, data) values ('{name}', '{expansion}', '{data}')"
#
def insertDataSummary(id_city, temperature, feels_like, wind, humidity):
    '''Заносим полученные данные в таблицу city'''
    return f"insert into summary (id_city, temperature, feels_like, wind, humidity) values ('{id_city}', '{temperature}', '{feels_like}', '{wind}', '{humidity}')"
#