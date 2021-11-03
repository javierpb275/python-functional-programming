# generators:

# generators allow us to generate a sequence of values over time
# generator is a special type of thing in python that allows us to use the keyword "yield"
# yield can pause and resume functions
# list() creates a giant list of for example 100 items in our computers memory
# example: range() creates those same items but one by one

def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result
# ----------------------------


def generator_function(num):
    for i in range(num):
        yield i*2


""" for item in generator_function(1000):
    print(item) """

g = generator_function(100)
next(g)
next(g)
print(next(g))  # 4
print(next(g))  # 6

print(g)  # <generator object generator_function at 0x000002BE4EB01E00>
