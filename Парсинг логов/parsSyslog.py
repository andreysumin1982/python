#-----------------------------------
import re
import os
import csv
import zipfile
#-----------------------------------
def readFile(path):
    '''ф-ция-генератор принимает путь и возвращает итератор'''
    with open(path) as file:
        for it in file.readlines():
            yield it
#-----------------------------------
def readFile_zip(path_archives):
    '''Ф-ция принимает путь к папке с архивами, смотрит содеожимое архива,
     распаковывает и возвр. список'''
    for z_file in os.listdir(path_archives):
        if zipfile.is_zipfile(f'{path_archives}{z_file}'):
            z = zipfile.ZipFile(f'{path_archives}{z_file}', 'r')
            print(z.namelist())
            #print(f'{path_archives}{"".join(z.namelist())}')
            z.extractall(f'{path_archives}{"".join(z.namelist())}') # распаковываем архив в папку с названием файла
            path = f'{path_archives}{"".join(z.namelist())}/{"".join(z.namelist())}'
            break
    with open(path) as file:
        return file.readlines()
#-------------------------------------
def saveParse_iis(path_read: str, path_save: str) -> csv:
    '''Ф-ция парсит файл {u_ex210730_log.txt} в словарь и записывает в .csv'''
    try:
        dict_cout = {} # Словарь для добавления времени, кол-ва запросов, ip/login.
        lst = [i for i in readFile(path_read) if '#' not in i[0]] # созд. список, отбрас. строки "#"
        for i in lst:
            #
            if i[11:19] not in dict_cout:
                if i.split()[7] == '-':
                    dict_cout[i[11:19]] = {'count':1, 'ip':[i.split()[8]]}
                else: dict_cout[i[11:19]] = {'count':1, 'ip':[i.split()[7]]}
            else:
                dict_cout[i[11:19]]['count'] += 1
                if i.split()[7] == '-':
                    dict_cout[i[11:19]]['ip'].append(i.split()[8])
                else: dict_cout[i[11:19]]['ip'].append(i.split()[7])
    except: pass
    # save in csv-file
    with open(path_save, 'w', newline='') as csv_file:
        write = csv.writer(csv_file, delimiter=';')
        write.writerow(['Время', 'Кол-во запросов', 'ip/login']) # Шапка
        for key, value in dict_cout.items():
            write.writerow([key, value['count'], ', '.join(value['ip'])])
        print(f'{path_save[-13:]} - выполнено.')
#--------------------------------------
#
#--------------------------------------
def readSyslog(lst: list, *args: str) -> print():
    '''Парсим syslog'''
    if args: # если передали аргумент для поиска.
        reg_exp = re.compile(r'\b{}'.format(*args)) # шаблон для поиска
        for j in (i.strip() for i in lst): # Выражение-генератор
            if re.findall(reg_exp, j):
                print(j)
    else: # иначе выводим весь syslog
        for j in (i.strip() for i in lst): # Выражение-генератор
            print(j)
#-----------------------------------
def run(path, *args):
    '''Ф-ция проверяет аргументы и передает их в ф-цию readSyslog(*args)'''
    with open(path) as file:
        if not args:
            return readSyslog(file.readlines())
        elif len(args) == 1:
            return readSyslog(file.readlines(), args[0])
        elif len(args) == 2:
            z = readFile_zip(path_syslogs_archives)
            readSyslog(z, args[0])
        else:
            print(f'Введено {args} - это болше 2 аргументов.')
            return
#-----------------------------------
if __name__ == '__main__':
    path_save_file = '/home/asumin/Документы/Программирование_Python/Для парсинга/parse_iis.csv'
    path_file_iis = '/home/asumin/Документы/Программирование_Python/Для парсинга/u_ex210730_log.txt'
    #
    path_file_syslog = '/home/asumin/Документы/Программирование_Python/Для парсинга/syslog.txt'
    path_syslogs_archives = '/home/asumin/Документы/Программирование_Python/Для парсинга/syslog-zip/'
    #
    #saveParse_iis(path_file_iis, path_save_file)
    #readFile_zip(path_syslogs_archives)

    run(path_file_syslog, 'vGP-0-3-1')