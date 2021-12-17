#Строка
a = {'set', 'str', 'dict', 'list'}
b = '.'.join(a)
print(b)
print(type(b))
#set,dict,list,str
#<class 'str'>

#Словарь
a = {('a', 2), ('b', 4)}
b = dict(a)
print(b)
print(type(b))
#{'b':4, 'a':2}
#<class 'dict'>

#Список
a = {1, 2, 0, 1, 3, 2}
b = list(a)
print(b)
print(type(b))
#[0, 1, 2, 3]
#<class 'list'>