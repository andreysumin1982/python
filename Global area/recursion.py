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
=======
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

#

#------------------------------------------------------
arr_keys = ['global','foo','bar','barz','bary','zoo','zoo2','zoo3','doo']
dict_namespace = {'global': {'parrent': 'global', 'var': {'qqq'}}, 'qqq': {'parrent': 'global', 'var': {'www'}}, 'www': {'parrent': 'qqq', 'var': {'eee'}}, 'eee': {'parrent': 'www', 'var': {'rrr'}}}
def add_recur(arr, d, count=0):
    if len(arr) == 0: return
    count +=1
    first = arr[0]
    d= {first: add_recur(arr[1:], count)}
    return d
#
print(add_recur(arr_keys, dict_namespace))


#  Подсказка для создания рекурсии для добавления в словарь.
'''dict_namespace['global'].update({'foo': {'parrent':'global'}})
print(dict_namespace)
dict_namespace['global']['foo'].update({'bar':{}})
print(dict_namespace)
dict_namespace['global']['foo']['bar'].update({'too':{}})
print(dict_namespace)'''
#
def read_recur(d):
    for k,v in d.items():
        if v['parrent'] == 5:
            print(k, v['parrent']); return
        else:
            read_recur(v['next->'])
#
#read_recur(dict_namespace)
#

#--
print('*'*20)
#dict_namespace = {'global': {'parrent': 'None', 'var': ['a','q']}, 'foo': {'parrent': 'global', 'var': ['b']}, 'boo': {'parrent': 'foo', 'var': ['c','b']}}
dict_namespace = {'global': {'parrent': 'global', 'var': {'qqq'}}, 'qqq': {'parrent': 'global', 'var': {'www'}}, 'www': {'parrent': 'qqq', 'var': {'eee'}}, 'eee': {'parrent': 'www', 'var': {'rrr'}}}
#arr_keys = ['global','foo','bar','barz','bary','zoo','zoo2','zoo3','doo']
arr_keys = ['global','qqq','www','eee']
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
'''test 15 
5
create first global
create second first
create third second 
add first my_var
get third my_var'''
#    Дописать try -  except ..
def test(name, namespace, d):    # Ф-ция для тестирования.
    list_key = arr_keys[::-1]
    #print(list_key)
    if name in list_key :
        if namespace in d[name]['var']:
            print(name); return
        else:
            index = list_key.index(name)
            for i in list_key[index:]:
                parrent = d[i]['parrent']
                if namespace in d[parrent]['var']:
                    print(parrent); return
                else: continue
            else: print('None'); return
#--
namespace = 'rrr'
name = 'www'
test(name, namespace, dict_namespace)
