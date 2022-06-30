# Импортируем класс PostgresSQL
from connectdb import Postgres
#
def run():
    # Экземпляр класса
    db = Postgres('localhost', 'drf_db', 'test', 'test')
    # Выполнить запрос
    db.executeRequest('SELECT version();')
    db.executeRequest('SELECT * FROM air;')
    #

#
if __name__ == '__main__':
    run()