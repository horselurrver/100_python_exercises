from ex33 import getList
"""
Define a function which can generate a list where the values are square of numbers between 1 and 20
(both included). Then the function needs to print all values except the first 5 elements in the list.
"""
def allButFirstFive():
    list = getList()
    print(str(list[5:]))
allButFirstFive()
