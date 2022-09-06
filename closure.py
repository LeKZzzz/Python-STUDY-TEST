# -*- coding: UTF-8 -*- 
# Creator：LeK
# Date：2022/9/6


def func(obj):  # 外部函数
    a = 1  # 外部函数的变量

    def func1():  # 内部函数
        obj[0] += a
        print(obj)

    return func1  # 返回内部函数


var = func([3, 2, 1, 0])  # 调用外部函数，通过返回值使变量var可以调用闭包函数
# 闭包函数封装了传递进去的数值，并且可以重复调用，调用后变化的数值仍然封装在闭包函数中供下一次调用
var()  # [4, 2, 1, 0]
var()  # [5, 2, 1, 0]
var()  # [6, 2, 1, 0]
