# Higher Order Function HOC
def greet(func):
    return func()


def greet2():
    def func():
        return 5
    return func()


print(greet(greet2))  # 5

# A higher order function is any function that either accepts a function as a parameter or returns a function.
