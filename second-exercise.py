# Write a short program that prints the numbers 1 to 10 using a for loop. 
# Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

import sys

# Rozwiązanie pętlą for
print('--- pętla for ---')
for i in range (1,11):
    print(i)
print()

# Rozwiązanie pętlą while 
print('--- pętla while ---')
i = 1
while i < 11:
    print(i)
    i = i + 1
print()
sys.exit()
