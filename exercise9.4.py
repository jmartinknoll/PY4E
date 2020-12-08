# Add code to the program in exercise 9.3 to figure out who has the
# most messages in the file. After all the data has been read and the dictionary has been created, 
# look through the dictionary using a maximum loop (see Chapter 5) to find who has
# the most messages and print how many messages the person has.

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File does not exist')
    quit()

value = dict()

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    email = words[1]
    value[email] = value.get(email, 0) + 1

max_value = None
max_email = None

if max_value is None:
    max_value = value[email]
    max_email = email
elif value[email] > max_value:
    max_value = value[email]
    max_email = email

#for k,v in address.items():
#    if address[email] > largest:
#        largest = address[email]
#        maxword = email

print(max_email, value[email])