"""
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

Hints:
Use set() to store a number of values without duplicate.
"""
lis = [12,24,35,24,88,120,155,88,120,155]
seen = set()
result = []

for item in lis:
    if item not in seen:
        seen.add(item)
        result.append(item)

print(result)
