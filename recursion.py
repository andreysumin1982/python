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
''' -------------- Пример заполнения словаря -----------
namesp = {
    'global': {
        'parent': None,
        'vars': set('a'),
        'foo': {
            'parent': 'global',
            'vars': set('b'),
            'bar': {
                'parent': 'foo', 
                'vars': set('a')}
        }
    }
}           ---------------------------------------
'''
print('-'*20)
arr_keys = ['global','foo','bar','barz','bary','zoo','zoo2','zoo3','doo']
dict_namespace = {}
def add_recur(arr, count = 0):
    if arr:
        first = arr[0]
        count +=1
        d = {first : {'parrent': count, 'next->' : add_recur(arr[1:], count)}}
        return d
#
dict_namespace = add_recur(arr_keys)
print(dict_namespace)
#
def read_recur(d):
    for k,v in d.items():
        if v['parrent'] == 5:
            print(k, v['parrent']); return
        else:
            read_recur(v['next->'])
#
read_recur(dict_namespace)
#--
print('*'*20)
dict_namespace = {'global': {'parrent': 'None', 'var': ['a','q']}, 'foo': {'parrent': 'global', 'var': ['b']}, 'boo': {'parrent': 'foo', 'var': ['c','b']}}
arr_keys = ['global','foo','bar','barz','bary','zoo','zoo2','zoo3','doo']
#
test6 = {'global': {'parrent': 'global', 'var': set()},
         'foo': {'parrent': 'global', 'var': set()},
         'bar': {'parrent': 'foo', 'var': {'b'}},
         'barz': {'parrent': 'bar', 'var': set()},
         'bary': {'parrent': 'barz', 'var': {'b'}},
         'zoo': {'parrent': 'bar', 'var': set()},
         'zoo2': {'parrent': 'zoo', 'var': set()},
         'zoo3': {'parrent': 'zoo2', 'var': set()},
         'doo': {'parrent': 'zoo', 'var': set()}}
#
def test(name, namespace, d):    # Ф-ция для тестирования.
    list_key = arr_keys[::-1]
    #print(list_key)
    if name in list_key :
        if namespace in d[name]['var']:
            print(name); return
        else:
            parrent = d[name]['parrent']
            if namespace in d[parrent]['var']:
                print(parrent); return
            else: print('None'); return
    else: print('None'); return
#--
namespace = 'b'
name = 'zoo'
test(name, namespace, test6)
