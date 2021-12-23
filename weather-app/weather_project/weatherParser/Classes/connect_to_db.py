import pyodbc
#
def connectDB():
    #db = pyodbc.connect('DRIVER={SQL Server}; SERVER=127.0.0.1;DATABASE=weather;UID=sa;PWD=#Demon159523021982;',
                        #timeout=3)
    q_conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=127.0.0.1;Database=weather;uid=SA;pwd=#Demon159523021982;Trusted_Connection=yes;", timeout=3)

    cursor = q_conn.cursor()
    return cursor