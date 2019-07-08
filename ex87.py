"""
Please write a program which count and print the numbers of each character in a string input by console.

Example:
If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1
"""
def countChars():
    dict = {}
    text = input()
    for char in text:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] = dict[char] + 1
    for key,value in dict.items():
        print('%s,%d'%(key, value))

countChars()
