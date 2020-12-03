# The following program counts the number of times the letter “a” appears in a string:
#
# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)
#
# Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

def counter(s, l):
    string = str(s)
    letter = str(l)
    count = 0
    for x in string:
        if x == letter:
            count = count + 1
    print(count)

counter('banana','a')