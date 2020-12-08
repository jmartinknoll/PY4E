# Write a program to read through a mail log, 
# build a histogram using a dictionary to count how many messages have come from
# each email address, and print the dictionary.

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File does not exist')
    quit()

address = dict()

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    email = words[1]
    address[email] = address.get(email, 0) + 1

print(address)