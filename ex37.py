"""
Write a program to generate and print another tuple whose values are even numbers
in the given tuple (1,2,3,4,5,6,7,8,9,10).
"""
def getEvens(userInput):
    result = []
    for num in userInput:
        if num % 2 == 0:
            result.append(num)
    print(tuple(result))

getEvens((1,2,3,4,5,6,7,8,9,10))
