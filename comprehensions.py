# list, set, dictionary

# list comprehensions:

my_list = [char for char in 'hello']
my_list2 = [num for num in range(0, 10)]
my_list3 = [num**2 for num in range(0, 10)]
my_list4 = [num**2 for num in range(0, 10) if num % 2 == 0]

""" print(my_list)  # ['h', 'e', 'l', 'l', 'o']
print(my_list2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list3)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(my_list4)  # [0, 4, 16, 36, 64] """

# set comprehensions:

my_set = {char for char in 'hello'}
my_set2 = {num for num in range(0, 10)}
my_set3 = {num**2 for num in range(0, 10)}
my_set4 = {num**2 for num in range(0, 10) if num % 2 == 0}

""" print(my_list)  # {'h', 'e', 'l', 'l', 'o'}
print(my_list2)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(my_list3)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
print(my_list4)  # {0, 4, 16, 36, 64} """

# dictionary comprehension:
simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

my_dict = {
    key: value**2 for key, value in simple_dict.items()
    if value % 2 == 0
}

my_dict2 = {num: num*2 for num in [1, 2, 3]}

""" print(my_dict)  # {'b': 4}
print(my_dict2)  # {1: 2, 2: 4, 3: 6} """

# comprehension exercise:

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))

print(duplicates)  # ['b', 'n']
