from functools import reduce

# lambda expressions: (anonymous functions)
my_list = [1, 2, 3]

result = reduce(lambda acc, item: acc+item, my_list)

# print(result)  # 6


# lambda exercise:


map_object = map(lambda num: num**2, [1, 2, 3])

squared_numbers_list = list(map_object)

print(squared_numbers_list)

# made the second key to be the sorting factor:
tuples_list = [(0, 2), (5, 2), (9, 9), (10, -1)]
tuples_list.sort(key=lambda tuple: tuple[1])

print(tuples_list)
