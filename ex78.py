"""
Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].
"""
list = [5,6,77,45,22,12,24]
list = [i for i in list if i % 2 != 0]
print(list)
