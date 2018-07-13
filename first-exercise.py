# Write code that prints Hello if 1 is stored in spam, prints Howdy 
# if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

import sys

spam = input()
spam = int(spam) # lub bez konwersji typów, wtedy w if-ach wymagany jest == '1' i == '2' 

if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')
sys.exit()