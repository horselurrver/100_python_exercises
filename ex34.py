from ex33 import getList

"""
Define a function which can generate a list where the values are square of numbers between 1 and 20
(both included). Then the function needs to print the last 5 elements in the list.
"""

def lastFive():
    list = getList()
    for i in range(5):
        print(list[len(list) - 1 - i])

lastFive()
