# Write a program which repeatedly reads numbers until the user enters “done”. 
# Once “done” is entered, print out the total, count, and average of the numbers. 
# If the user enters anything other than a number, detect their mistake using try and except 
# and print an error message and skip to the next number.
count = 0
total = 0.0
# total is needed to calculate the average (total/count)

while True:
    x = input('Enter a number: ')
    if x == 'done':
        break
    try:
        n = float(x)
    except:
        print('invalid input')
        continue
    count = count + 1
    total = total + n

print('Done!')
print('Total:',total,'Count:',count,'Average:',total/count)