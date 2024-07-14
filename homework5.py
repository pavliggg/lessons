immutable_var = 'power', 1 , 1.5, False, ["bowl", "axe"]
print(immutable_var)
print(immutable_var [0])
print(immutable_var [1])
print(immutable_var [2])
print(immutable_var [2:5])
immutable_var [4] [0] = "weak" # Кортеж изменить можно, только если внутри переменной будет список.
print(immutable_var)
mutable_list = ["Bow", "Sword", 60, "Arrows", False]
print (mutable_list)
mutable_list.remove(False)
print (mutable_list)
mutable_list [0] = "Arbalet"
mutable_list [3] = "Bolts"
print (mutable_list)