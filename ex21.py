import re
import math
"""
Question£º
A robot moves in a plane starting from the original point (0,0).
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps.
Please write a program to compute the distance from current position after
a sequence of movement and original point. I
f the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
"""
def getInput():
    result = []
    prog = re.compile('(UP|DOWN|LEFT|RIGHT) \d')
    while True:
        line = input()
        if not line:
            break
        if not prog.match(line):
            print('Invalid input')
        else:
            result.append(line)
    return result

def calcDistance():
    instructions = getInput()
    horizontal = 0
    vertical = 0
    for instruction in instructions:
        instruction = instruction.split(' ')
        distance = int(instruction[1])
        direction = instruction[0]
        if direction == 'UP':
            vertical += distance
        elif direction == 'DOWN':
            vertical -= distance
        elif direction == 'LEFT':
            horizontal -= distance
        else:
            horizontal += distance
    dist = round(math.sqrt(horizontal * horizontal + vertical * vertical))
    print(dist)

calcDistance()
