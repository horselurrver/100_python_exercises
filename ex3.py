"""
    With a given integral number n, write a program to generate a dictionary that
    contains (i, i*i) such that is an integral number between i and n
    (both included), and then the program should print the dictionary.
"""
def generateDictionary(num):
    result = {}
    for i in range(num):
        result[i + 1] = (i + 1) * (i + 1)
    return result

# get numbers 1 through 10 to try out with this function
numbers = [i + 1 for i in range(10)]
print(numbers)
for num in numbers:
    print(generateDictionary(num))
