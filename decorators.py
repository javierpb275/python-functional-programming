# Decorators

def my_decorator(func):
    def wrap_func():
        print('*************')
        func()
        print('*************')
    return wrap_func


@my_decorator
def hello():
    print('hello')


hello()


""" hello2 = my_decorator(hello)
hello2()
my_decorator(hello)() """
