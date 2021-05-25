'''Задачи stepic.org.  Модули и импорт'''
import module1
import module2

print(3)
#-------------------------------------------
import datetime
from datetime import timedelta
#
PATH = '/home/asumin/Документы/Программирование Python/stepik.org/Основы и применение/Модули/test'
#
def read_file(path_file):
    with open(path_file) as file:
        return [i.strip() for i in file.readlines()]
print(read_file(PATH))

def run():
   p = read_file(PATH)[0].split(' ')
   p2 = read_file(PATH)[1].split(' ')
   #
   year = int(p[0])
   month = int(p[1])
   day = int(p[2])
   #
   p_days = int(p2[0])
   p_date = datetime.date(year, month, day)
   delta = datetime.timedelta(p_days)
   p_date += delta

   print(p_date.strftime("%Y %m %d").replace(' 0', ' '))
run()
#------ Реализация для Stepic (Simple in / out )----------

'''p_date = input(': ').split()
p_days = int(input(': '))
#
year = int(p_date[0])
month = int(p_date[1])
day = int(p_date[2])
#
p_date = datetime.date(year, month, day)
delta = datetime.timedelta(p_days)
p_date += delta
#
print(p_date.strftime("%Y %m %d").replace(' 0', ' '))'''

#---------------------------------------------------------
'''Задача про Алису и зашифрованную информацию
Алиса владеет интересной информацией, которую хочет заполучить Боб.
Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.

Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями, но он не смог понять какой из паролей ему нужен. Помогите ему решить эту проблему.

Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.

Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать, какой из паролей служит ключом для расшифровки файла с интересной информацией.
Ответом для данной задачи служит расшифрованная интересная информация Алисы.

Файл с информацией
Файл с паролями

Примечание:
Для того, чтобы считать все данные из бинарного файла, можно использовать, например, следующий код:
--------------------------------------------
with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()'''
#
from simplecrypt import DecryptionException, decrypt
PATH = '/home/asumin/Документы/Программирование Python/stepik.org/Основы и применение/Модули/encrypted.bin'
PASS = '/home/asumin/Документы/Программирование Python/stepik.org/Основы и применение/Модули/passwords.txt'
#
def read_bin(path_file):
   with open(path_file, 'rb') as file:
      return file.read().strip()
#print(read_bin(PATH))
#
def read_txt(path_file):
   with open(path_file, 'r') as file:
      return file.readlines()
#print(read_txt(PASS))
#
for i_pass in read_txt(PASS):
   try:
      print(decrypt(i_pass.strip(), read_bin(PATH)).decode('utf8'))
   except:
      DecryptionException
      print(i_pass, 'is wrong')
   else:
      print(i_pass, 'in correct')
#---------------------------------------------------------------------------------
