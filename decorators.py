# -*- coding: UTF-8 -*- 
# Creator：LeK
# Date：2022/9/6


def func1(type):
    def func2(func):
        def func3(x, y):
            if type == 1:
                print('各+5')
                x += 5
                y += 5
            else:
                print('各+10')
                x += 10
                y += 10
            return func(x, y)

        return func3

    return func2


@func1(type=1)
def myprint1(x, y):
    print(x, y)


@func1(type=2)
def myprint2(x, y):
    print(x, y)


myprint1(5, 5)
myprint2(5, 5)

'''
各+5
10 10
各+10
15 15
'''