import random
"""
Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
"""
list = [i for i in range(100, 201) if i % 2 == 0]
print(random.sample(list, 5))
