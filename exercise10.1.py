# Revise a previous program as follows: Read and parse the
# “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits
# by creating a list of (count, email) tuples from the dictionary. Then
# sort the list in reverse order and print out the person who has the most
# commits.

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

#print(address)

lst = list()
for k,v in list(address.items()):
    lst.append((v,k))

lst.sort(reverse=True)

for v,k in lst[:1]:
    print(k,v)

