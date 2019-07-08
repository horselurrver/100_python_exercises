"""
Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

Hint:
Use for loop to iterate all possible solutions.
"""
def numRabbitsChickens(heads, legs):
    for i in range(heads): # i is the number of chickens, heads - i is the number of rabbits
        totalLegs = 4 * (heads - i) + 2 * i
        if totalLegs == legs:
            print('%d chickens, %d rabbits'%(i, heads - i))
            break

numRabbitsChickens(35, 94)
