def showTable(tableName):
    '''Смотрим содержимое таблицы'''
    return f'select * from {tableName}'
#
def insertData(cityName, imageName, expansion, description):
    '''Заносим полученные данные в таблицы'''
    return f"insert into city (name) values ('{cityName}')" \
           f"insert into image (name, expansion) values ('{imageName}', '{expansion}')" \
           f"insert into osadki (description) values ('{description}')"
    #f'insert into city (name) values ({name})'

    pass
