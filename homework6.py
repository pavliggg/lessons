my_dict = {'Pavel': 1992, 'Denis': 1995, 'Sofia': 1993}
print(my_dict)
print(my_dict.get('Pavel'))
my_dict.get('Dmitriy')
my_dict.update({'Dmitriy': 1997, 'Rick': 1969})
print(my_dict.pop('Denis', 1995))
print(my_dict)
my_set = {35, 22, 32, 11, 11, 19, 'Alex', 'Alex', 17, 19, 35}
print(my_set)
my_set.update([177, True])
my_set.discard(35)
print(my_set)