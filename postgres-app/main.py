#
from connectdb import Postgres
#
def run():
    db = Postgres('localhost', 'cities', 'test', 'test')
    # Выполнить запрос
    db.executeRequest('SELECT version();')
    db.executeRequest('SELECT * FROM name_of_the_cities;')
    # Смотрим № транзакций:
    # Строка создана прудыдущей транзакцией, а xmax = 0 означает, что эта версия актуальна.
    db.executeRequest('SELECT *, xmin, xmax FROM name_of_the_cities')


#
if __name__ == '__main__':
    run()