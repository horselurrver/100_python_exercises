import re
"""
Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
"""
def bankTransaction():
    total = 0
    while True:
        line = input()
        regexp = re.compile('(D|W) \d+')
        if not regexp.match(line):
            if line == '':
                break
            print('Invalid input')
            continue
        if line[0] == 'D':
            total = total + int(line.split(' ')[1])
        else:
            update = int(line.split(' ')[1])
            if (total - update) < 0:
                print('You only have ${}!'.format(total))
            else:
                total = total - update
    print('${}'.format(total))

bankTransaction()
