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


my_list = make_list(100)

print(my_list)
