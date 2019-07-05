"""
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""
def calcNum(input):
    sum = 0
    for i in range(4):
        sum = sum + int(input * (i + 1))
    print(sum)

calcNum('9')
