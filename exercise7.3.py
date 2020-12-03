# Sometimes when programmers get bored or want to have a
# bit of fun, they add a harmless Easter Egg to their program. Modify
# the program that prompts the user for the file name so that it prints a
# funny message when the user types in the exact file name “na na boo
# boo”. The program should behave normally for all other files which
# exist and don’t exist.

fname = input('Enter a file name: ')
if fname == 'na na boo boo':
    print('you belong in a garbage can')
    quit()
try:
    fhand = open(fname)
except:
    print('File does not exist')
    quit()

count = 0
total = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        x = line.find(':')
        y = line[x + 1: ]
        z = float(y)
        count = count + 1
        total = total + z

print('There are',count,'subject lines')