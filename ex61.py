"""
Please write a program using generator to print the even numbers between 0 and n
in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10
"""
def nextEven(stop):
    i = 0
    while True:
        if i <= stop:
            yield(i)
        else:
            break
        i = i + 2

result = []
stop = ''
while True:
    stop = int(input('Please enter a number greater than or equal to zero: '))
    if stop > 0 or stop == 0:
        break
for num in nextEven(stop):
    result.append(str(num))

print(','.join(result))
