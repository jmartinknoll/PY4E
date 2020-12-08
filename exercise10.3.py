# Write a program that reads a file and prints the letters
# in decreasing order of frequency. Your program should convert all the
# input to lower case and only count the letters a-z. Your program should
# not count spaces, digits, punctuation, or anything other than the letters
# a-z. Find text samples from several different languages and see how
# letter frequency varies between languages. Compare your results with
# the tables at https://wikipedia.org/wiki/Letter_frequencies.

import string
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File does not exist')
    quit()

di = dict()

total = 0
for line in fhand:
    line = line.strip()
    line = line.replace('\t','')
    line = line.replace(' ','')
    line = line.translate(str.maketrans('','',string.punctuation))
    line = line.translate(str.maketrans('','',string.digits))
    line = line.lower()
    for letter in line:
        di[letter] = di.get(letter,0) + 1
        total += 1
#print(di)

lst = list()
for k,v in list(di.items()):
    lst.append((k,v))

lst.sort()

for k,v in lst:
    frequency = v / total
    print(k,v,frequency)

#for v in di.values():