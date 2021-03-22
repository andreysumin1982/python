arr = [1,'w',3,'c',5,'g',7,8,9,10,11,12,'s',14,'b']
#
def recurse_dict_2(arr):
    if arr:
        fist = arr[0]
        d = {fist : recurse_dict_2(arr[1:]) }
        return d
print(recurse_dict_2(arr))
print('*' * 30)
#
def recurse_dict_3(defain):
    try:
        for k,v in defain.items():
            print(k, end=' ')
            recurse_dict_3(v)
    except: print()
#
arr_p = []
arr.append(recurse_dict_3(recurse_dict_2(arr)))
print(arr[:-1])
#--
n= 1
for i in range(1, 5+1):
    n *= i  #   Факториал
    print(n)
#
def fac(f): #  Рекурсия факториала
    if f != 0:
        return f*fac(f-1)
    return 1
print(fac(3))
#--  Выводим элементы списка рекурсией (без цикла)
arr = [1,'a',3,'z',5]
def reverse(n, k=0):  # k=0, не обязaтельный аргумент
    if k != len(n):
        print(n[k])
        k+=1
        reverse(n, k)
reverse(arr)
#--
print('*'*20)
dict_namespace = {'global': {'parrent': 'None', 'var': ['a','x']}, 'foo': {'parrent': 'global', 'var': ['b']}, 'boo': {'parrent': 'foo', 'var': ['c','d']}}
arr_keys = ['global','foo','boo']
#
def recurse2(name, namespace, d):    # Ф-ция (рекурсией) ищет в словаре ключи и значения.
    list_key = arr_keys[::-1]
    for index, element in enumerate(list_key):
        if name == element:
            count = 0
            while count < len(list_key[index:]):
                if namespace not in d[list_key[count]]['var']:
                    count += 1
                    if count == len(list_key[index:]):
                        print('None'); break
                elif namespace in d[list_key[count]]['var']:
                    print(list_key[count]); break
#--
namespace = '1'
name = 'boo'
recurse2(name, namespace, dict_namespace)
