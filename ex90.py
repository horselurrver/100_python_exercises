"""
Please write a program which prints all permutations of [1,2,3]


Hints:
Use itertools.permutations() to get permutations of list.
"""

def getPermutations(array):
    if len(array) == 0:
        return []
    if len(array) == 1:
        return [array]

    allPermutations = []
    for i in range(len(array)):
        firstElement = array[i]
        remainingList = array[:i] + array[i + 1:]
        for permutation in getPermutations(remainingList):
            allPermutations.append([firstElement] + permutation)

    return allPermutations

for permutation in getPermutations([1, 2, 3, 4, 5]):
    print(permutation)
