# error handling

def error_handling1():
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

# error_handling1()

# error handling 2:


def sum(num1, num2):
    try:
        return num1 + num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)


#print(sum('a', 2))


# error handling 3:

def error_handling3():
    while True:
        try:
            age = int(input("what's your age?"))
            10/age
        except ValueError:
            print('please enter a number')
            continue
        except ZeroDivisionError:
            print('please enter a number bigger than 0')
            break
        else:
            print('thank you')
        finally:
            print('ok, i am done')
        print('can you hear me?')


error_handling3()
