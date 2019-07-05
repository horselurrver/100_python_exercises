"""
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
def getNumbers():
    result = []
    for i in range(1000, 3001):
        string = str(i)
        allDigitsEven = True
        for char in string:
            if int(char) % 2 != 0:
                allDigitsEven = False
        if allDigitsEven:
            result.append(str(i))
    print(', '.join(result))

getNumbers()
