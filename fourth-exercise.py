# Comma Code
# Write a function that takes a list value as an argument and returns a string with all the 
# items separated by a comma and a space, with and inserted before the last item. 
# For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. 
# But your function should be able to work with any list value passed to it.

import sys

def divider(listToSeparate):
    for i in range(len(listToSeparate)- 1):
        print(listToSeparate[i] + ' ', end='')
    print('and ' + listToSeparate[-1])

spam = ['apples', 'bananas', 'tofu', 'cats', 'kappa', 'A', 'B', 'C', 'D']
divider(spam)
sys.exit()