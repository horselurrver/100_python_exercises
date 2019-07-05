"""
    Write a program which accepts a sequence of comma-separated numbers
    from console and generate a list and a tuple which contains every number
"""
def listAndTuple(input):
    splitUp = input.split(', ')
    joined = ''.join(splitUp)
    if joined.isdigit():
        lis = splitUp
        tup = tuple(lis)
        print('List: ' + str(lis))
        print('Tuple: ' + str(tup))
    else:
        print('Invalid input')

input = input('Enter numbers separated by commas ')
listAndTuple(input)
