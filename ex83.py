"""
By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].
"""
list = [12,24,35,24,88,120,155]
list = [i for i in list if i != 24]
print(list)
