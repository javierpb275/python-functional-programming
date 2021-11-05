def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break


#special_for([1, 2, 3])

""" 
<list_iterator object at 0x000002DB8DDC21D0>
1
<list_iterator object at 0x000002DB8DDC21D0>
2
<list_iterator object at 0x000002DB8DDC21D0>
3
<list_iterator object at 0x000002DB8DDC21D0>
 """


class MyGen():

    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 10)
for i in gen:
    print(i)
