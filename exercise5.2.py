# Write a program which repeatedly reads numbers until the user enters “done”. 
# Once “done” is entered, print out the total, count, and average of the numbers. 
# If the user enters anything other than a number, detect their mistake using try and except 
# and print an error message and skip to the next number.

# Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average.

count = 0
total = 0.0
largest = None
smallest = None

while True:
    x = input('Enter a number: ')
    if x == 'done':
        break
    try:
        n = float(x)
    except:
        print('invalid input')
        continue
    
    if smallest is None:
        smallest = n
    elif n < smallest:
        smallest = n
    
    if largest is None:
        largest = n
    elif n > largest:
        largest = n

    count = count + 1
    total = total + n

print('Done!')
print('Total:',total,'Count:',count,'Smallest:',smallest,'Largest:',largest)