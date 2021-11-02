# error handling

""" while True:
    try:
        age = int(input("what's your age?"))
        10/age
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter a number bigger than 0')
    else:
        print('thank you')
        break
 """

# error handling 2:


def sum(num1, num2):
    try:
        return num1 + num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)


print(sum('a', 2))
