"""
Write a program which can filter() to make a list whose elements are even number
between 1 and 20 (both included).
"""
def getEvens():
    onetwenty = [i for i in range(1, 21)]
    evens = list(filter(lambda x : x % 2 == 0, onetwenty))
    print(evens)

getEvens()
