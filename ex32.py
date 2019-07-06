"""
Define a function which can print a dictionary where the keys are numbers between 1 and 20
(both included) and the values are square of keys.
"""
def printDict():
    dict = {}
    for i in range(20):
        dict[i + 1] = (i + 1) ** 2
    for key in dict.keys():
        print(key)

printDict()
