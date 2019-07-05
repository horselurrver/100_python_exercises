"""
    Write a program which can compute the factorial of a given number.
    The results should be printed in a comma-separated sequence on a single line.
    Suppose the following input is supplied to the program:
    8
    Then, the output should be:
    40320
"""
def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

# get numbers 1 through 10 to try out with the factorial function
numbers = [i + 1 for i in range(10)]
for num in numbers:
    print(factorial(num))
