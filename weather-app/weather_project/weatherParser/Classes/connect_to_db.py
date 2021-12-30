import pyodbc
#
def connectDB():

    '''Ф-ция подключается к базе SQL "weather" и возвращает cursor '''
    connect = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                             "Server=127.0.0.1;"
                             "Database=weather;"
                             "uid=SA;"
                             "pwd=#Demon159523021982;"
                             "Trusted_Connection=no;",
                             timeout=3)
    #
    cursor = connect.cursor()
    return cursor # Возвращает обьект
#---
def getFetchall(sql_request): ######### Доделать ф-цию !!!!!
    ''' Ф-ция возвращает результат sql-запроса'''
    db = connectDB()
    db.execute(sql_request)
    result = db.fetchall()
    db.close()
    return result
#---
def insertData(sql_request):
    db = connectDB()
    db.execute(sql_request)
    db.commit()
    db.close()
    return
#---
def deleteData(sql_request):
    db = connectDB()
    db.execute(sql_request)
    db.commit()
    db.close()
    return