import random
"""
Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
"""
list = [random.randint(100, 200) for i in range(5)]
print(list)
