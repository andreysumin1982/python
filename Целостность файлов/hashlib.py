'''Дан файл, содержащий имена файлов, алгоритм хэширования (один из MD5/SHA1/SHA256) и соответствующие им хэш-суммы,
вычисленные по соответствующему алгоритму и указанные в файле через пробел.
Напишите программу, читающую данный файл и проверяющую целостность файлов.
Пример
Файл сумм:
file_01.bin md5 aaeab83fcc93cd3ab003fa8bfd8d8906
file_02.bin md5 6dc2d05c8374293fe20bc4c22c236e2e
file_03.bin md5 6dc2d05c8374293fe20bc4c22c236e2e
file_04.txt sha1 da39a3ee5e6b4b0d3255bfef95601890afd80709
Пример вызова:
<your program> <path to the input file> <path to the directory containing the files to check>
Формат вывода:
file_01.bin OK
file_02.bin FAIL
file_03.bin NOT FOUND
file_04.txt OK'''
#
import hashlib
import os
#
def hash_files(path_file_hash_sum, path_files_to_check):
    if not os.path.isfile(path_file_hash_sum): # Проверяем на на личие файла с хеш-суммами.
        return print(f'Файл не найден.')
    with open(path_file_hash_sum) as file:
        for name in file.readlines():
            # Читаем файл и в цикле бежим по строкам.
            file_name = name.strip().split()[0] # имя файла
            hash_file = name.strip().split()[1] # хеш (md5, sha1,.,)
            check_sum = name.strip().split()[2] # контр. сумма
            #
            # Метод algorithms_available создает список всех алгоритмов шифрования
            # Добавляю в словарь  {'хеш' : hashlib.new(i) - Функция new() принимет имя в качестве строки желаемого алгоритма хеширования как первый параметр}
            dict_hash = {i : hashlib.new(i) for i in hashlib.algorithms_available}
            #
            if hash_file in dict_hash:
                h = dict_hash[hash_file]
                #print(h.name)
                if not os.path.isfile(f'{path_files_to_check}/{file_name}'):
                    print(f'{file_name} NOT FOUND')
                    continue
                #
                with open(f'{path_files_to_check}/{file_name}', 'rb') as fil:
                    while True:
                        data = fil.read(1024)
                        if not data:
                            break
                        h.update(data)
                        #print(f'{file_name} - {h.hexdigest()}')
                        if check_sum == h.hexdigest():
                            print(f'{file_name} OK')
                        else:
                            print(f'{file_name} FAIL')
#
if __name__=='__main__':
   #
   path_file = '/home/asumin/Документы/Программирование_Python/test_files/hashfile.txt'
   path_file_check = '/home/asumin/Документы/Программирование_Python/test_files'
   #
   hash_files(path_file, path_file_check) # Вызываем ф-цию.
   