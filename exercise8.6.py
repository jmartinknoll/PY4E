# Rewrite the program that prompts the user for a list of
# numbers and prints out the maximum and minimum of the numbers at
# the end when the user enters “done”. 
# 
# Write the program to store the numbers the user enters in a list 
# and use the max() and min() functions to compute 
# the maximum and minimum numbers after the loop completes.

lst = list()

while True:
    x = input('Enter a number: ')
    if x == 'done':
        break
    try:
        n = float(x)
        lst.append(n)
    except:
        print('invalid input')
        continue
    
print('Maximum:',max(lst))
print('Minimum:',min(lst))
