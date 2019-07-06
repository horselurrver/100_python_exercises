"""
Define a function which can generate and print a list where the values are square of numbers
between 1 and 20 (both included).
"""
def getList():
    list = [i ** 2 for i in range(1, 21)]
    return list

if __name__ == "__main__":
    print(getList())
