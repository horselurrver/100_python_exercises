"""
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""
def calcNum(userInput):
    numLetters = 0
    numDigits = 0
    for char in userInput:
        if char.isalpha():
            numLetters = numLetters + 1
        elif char.isdigit():
            numDigits = numDigits + 1
    print('LETTERS {}'.format(numLetters))
    print('DIGITS {}'.format(numDigits))

calcNum('hello world! 123')
