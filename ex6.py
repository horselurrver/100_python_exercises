import math
"""
    Write a program that calculates and prints the value according to the given formula:
    Q = Square root of [(2 * C * D)/H]
    Following are the fixed values of C and H:
    C is 50. H is 30.
    D is the variable whose values should be input to your program in a comma-separated sequence.
"""
# input is an array, with values C, D, and H respectively
def calculate(input):
    result = ''
    letterC = 50
    letterH = 30
    for letterD in input:
        print(int(math.sqrt((2 * letterC * letterD) / letterH)))

valid = True
user = ''
while True:
    user = input('Enter comma-separated numbers ')
    user = user.split(',')
    valid = True
    for i in user:
        try:
            num = int(i)
        except ValueError:
            valid = False
    if valid:
        break
        
user = [int(i) for i in user]
calculate(user)
