# Импортируем класс PostgresSQL
from connectdb import Postgres
#
def run():
    # Экземпляр класса
    db = Postgres('localhost', 'drfapi_db', 'test', 'test')
    # Выполнить запрос
    db.executeRequest('SELECT version();')
    db.executeRequest('SELECT table_name FROM information_schema.tables;')
    db.executeRequest('SHOW DATABASES;')
    #

#
if __name__ == '__main__':
    run()