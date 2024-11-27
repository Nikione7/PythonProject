# Словарь
my_dict = { 'Nik': 2003, 'Masha': 2000, 'Max': 1999 }
print(my_dict)
print(my_dict.get('Nik'))
my_dict.update({'Eva': 2005, 'Vasya': 1990})
a = my_dict.pop('Eva')
print(my_dict)
print(a)
print(my_dict)
# Множество
my_set = {1,2,3,4,1,3,2,7,5,7,'car', False}
print(my_set)
print(my_set.add(8))
print(my_set.add(9))
print(my_set.remove(1))
print(my_set)