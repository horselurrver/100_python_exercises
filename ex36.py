from ex33 import getList
"""
Define a function which can generate and print a tuple where the value are
square of numbers between 1 and 20 (both included).
"""
def getTuple():
    list = getList()
    list = tuple(list)
    print(list)

getTuple()
