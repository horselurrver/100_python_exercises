"""
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""
def calcCases(input):
    upper = 0
    lower = 0
    for char in input:
        if char.isupper():
            upper = upper + 1
        elif char.islower():
            lower = lower + 1
    print('UPPER CASE {}'.format(upper))
    print('LOWER CASE {}'.format(lower))

calcCases('Hello world!')
