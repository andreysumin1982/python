# connect_db
import psycopg2
from psycopg2 import Error
#
class Postgres:
    #
    def __init__(self, host, dbname, user, password):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        # Подключение к базе данных
        try:
            self.connectdb = psycopg2.connect(f"host={host} "
                                       f"dbname={dbname} "
                                       f"user={user} "
                                       f"password={password}")
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL:", error)
            self.connectdb.close()
        else:
            print(f'{"*"*40}\nСоединение с PostgreSQL установлено.\n'
                  f'Вы подключены к базе данных "{dbname}".\n{"*"*40}')
    #
    def executeRequest(self, request):
        try:
            # Курсор для выполнения операций с базой данных
            self.cursor = self.connectdb.cursor()
            # Выполнение SQL-запроса
            self.cursor.execute(request)
            # Получить результат
            record = self.cursor.fetchone()
            print(record)
        except (Exception, Error) as error:
            print(f"{'-'*40}\nПользователь: {self.user}\n{error}{'-'*40}")
        else:
            print('Запрос выполнен')
    #
    def __del__(self):
        # Закрыть соединение с базой
        self.cursor.close()
        self.connectdb.close()
        print("Соединение с PostgreSQL закрыто.")
#