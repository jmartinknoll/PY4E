# This program counts the distribution of the hour of the day
# for each of the messages. You can pull the hour from the “From” line
# by finding the time string and then splitting that string into parts using
# the colon character. Once you have accumulated the counts for each
# hour, print out the counts, one per line, sorted by hour as shown below.

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
    time = words[5]
    hour = time.split(':')[0]
    di[hour] = di.get(hour, 0) + 1

#print(di)

lst = list()
for k,v in list(di.items()):
    lst.append((k,v))

lst.sort()

for k,v in lst:
    print(k,v)