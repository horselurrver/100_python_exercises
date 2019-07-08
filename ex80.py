"""
By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
"""
list = [12,24,35,70,88,120,155]
list = [value for index, value in enumerate(list) if index != 0 and index != 2 and index != 4 and index != 6]
print(list)
