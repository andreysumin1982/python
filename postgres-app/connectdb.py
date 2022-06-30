# connect_db
import psycopg2
from psycopg2 import Error

#
class Postgres:
    #
    def __str__(self):
        return "* Класс Postgres создан, для работы с базами данных PostgreSQL *"
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
            print(f'{"-"*60}\nСоединение с PostgreSQL установлено.\n'
                  f'Пользователь {self.user} '
                  f'подключен к базе данных "{dbname}".\n{"-"*60}')
    #
    def executeRequest(self, request):
        try:
            # Курсор для выполнения операций с базой данных
            self.cursor = self.connectdb.cursor()
            # Выполнение SQL-запроса
            self.cursor.execute(request)
            # Получить результат
            result = self.cursor.fetchall()
        except (Exception, Error) as error:
            print(error); return error
        else:
            print(f'Выполнен запрос: {request}')
            self.acceptRequest(result)

    #
    def transactionCommit(self):
        self.connectdb.commit()
        print("Транзакция успешно завершена.")
    #
    def transactionRollback(self):
        self.connectdb.rollback()
        print("Ошибка в транзакции. Отмена всех остальных операций транзакции.")
    #
    def acceptRequest(self, request):
        d = {}
        for key, value in enumerate(request):
            if key not in d:
                d[key] = list(map(lambda x:str(x), value))
                print(' '.join(d[key]))
        print()
    #
    @staticmethod
    def testMethod(*args):
        s1,s2,s3 = 1, 1, 1
        for i in args:
            s1 +=i
        s2 = s1 * 500
        s3 = s2 // s1
        return s1, s2, s3
    #
    def __del__(self):\
        # Закрыть соединение с базой
        self.cursor.close()
        self.connectdb.close()
        print(f'{"-" * 60}\n'
              f'Соединение с PostgreSQL закрыто.\n'
              f'Пользователь {self.user} отключен от базы данных {self.dbname}.\n'
              f'{"-" * 60}')
#