#
from connectdb import Postgres
#
def run():
    db = Postgres('localhost', 'drf_db', 'user', 'user')
    # Выполнить запрос
    db.executeRequest('SELECT version();')
    db.executeRequest('SELECT * FROM users;')

#
if __name__ == '__main__':
    run()