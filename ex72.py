import random
"""
Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.
"""
list = [i for i in range(1, 1001) if i % 7 == 0 and i % 5 == 0]
print(random.sample(list, 5))
