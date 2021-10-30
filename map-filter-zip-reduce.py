from functools import reduce

#map, filter, zip and reduce

my_list = [1, 2, 3]
your_list = [10, 20, 30]

# map:


def multiply_by2(item):
    return item*2


map_object = map(multiply_by2, my_list)

print(map_object)  # <map object at 0x0000015D43AC2230>
print(list(map_object))  # [2, 4, 6]


# filter:


def check_odd(number):
    return number % 2 != 0


filter_object = filter(check_odd, my_list)

print(filter_object)  # <filter object at 0x000001FC178B2FB0>
print(list(filter_object))  # [1, 3]

# zip:

zip_object = zip(my_list, your_list)

print(zip_object)  # <zip object at 0x000001BC6E6B0240>
print(list(zip_object))  # [(1, 10), (2, 20), (3, 30)]

# reduce:


def accumulator(acc, item):
    return acc + item


reduce_result = reduce(accumulator, my_list, 0)

print(reduce_result)  # 6
