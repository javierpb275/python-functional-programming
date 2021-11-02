# error handling

while True:
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
