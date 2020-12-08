# This program records the domain name (instead of the
# address) where the message was sent from instead of who the mail came
# from (i.e., the whole email address). At the end of the program, print
# out the contents of your dictionary.

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File does not exist')
    quit()

di = dict()

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    email = words[1]
    domain = email.split('@')[1]
    di[domain] = di.get(domain, 0) + 1

# could shorten words = line.split() and email = words[1] lines to just:
# email = line.split()[1]

print(di)