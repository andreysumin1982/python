#
from connectdb import Postgres
#
def run():
    db = Postgres('localhost', 'cities', 'test', 'test')
    # Выполнить запрос
    db.executeRequest('SELECT version();')
    db.executeRequest('SELECT * FROM weather;')

#
if __name__ == '__main__':
    run()