"""
Define a function that can receive two integral numbers in string form
and compute their sum and then print it in console.
"""
def sum(string1, string2):
    total = int(string1) + int(string2)
    print(total)
    return total

sum('100', '20')
