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
#
def recurse2(d):    # Ф-ция (рекурсией) ищет в словаре ключи и значения.
    for key, value in d.items():
        #print(key)
        try:
            if 'd' in d[key]['var']:
                print(key, value['var'])
            recurse2(value)
        except: pass

recurse2(dict_namespace)
