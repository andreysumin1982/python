import pyodbc
#
def connectDB():
<<<<<<< HEAD
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
    return cursor
def connectxui():
    pass
=======
    #db = pyodbc.connect('DRIVER={SQL Server}; SERVER=127.0.0.1;DATABASE=weather;UID=sa;PWD=#Demon159523021982;',
                        #timeout=3)
    q_conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                            "Server=127.0.0.1;"
                            "Database=weather;"
                            "uid=SA;"
                            "pwd=#Demon159523021982;"
                            "Trusted_Connection=no;",
                            timeout=3)

    cursor = q_conn.cursor()
    return cursor
>>>>>>> 7045ac5dd58d62f5736557f3c54987e3e509652d
