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
def getFetchall(sql_request):
    '''Ф-ция возвращает результат sql-запроса'''
    db = connectDB()
    data = db.execute(sql_request)
    result = data.fetchall()
    db.close()
    return result
#---