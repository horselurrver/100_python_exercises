"""
Please write a binary search function which searches an item in a sorted list.
The function should return the index of element to be searched in the list.


Hints:
Use if/elif to deal with conditions.
"""

def binarySearch(list, toSearch):
    list.sort()
    print('The list: ' + str(list))
    beginning = 0
    end = len(list) - 1
    index = (beginning + end) // 2
    while index != 0 or index != len(list) - 1:
        #print('Current index: ' + str(index))
        if list[index] == toSearch:
            return index
        elif list[end] == toSearch:
            return end
        elif list[beginning] == toSearch:
            return beginning
        elif end == beginning + 1:
            return str(toSearch) + ' is not in list'
        elif toSearch > list[index]:
            beginning = index
        else:
            end = index
        index = (beginning + end) // 2

print(binarySearch([2,5,7,9,11,17,222], 90))
