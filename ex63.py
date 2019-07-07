"""
Please write assert statements to verify that every number in the list [2,4,6,8] is even.

Hints:
Use "assert expression" to make assertion.
"""
list = [i for i in range(2, 9) if i % 2 == 0]
for num in list:
    assert num % 2 == 0
