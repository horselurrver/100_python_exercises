"""
By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
"""
eight = [0 for i in range(8)]
five = [eight for i in range(5)]
three = [five for i in range(3)]
print(three)
