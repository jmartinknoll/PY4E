# prompt for score between 0.0 and 1.0
# error message for score that is out of range
# print a letter grade using the following table:
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F

x = input('Enter score (0.0 - 1.0):')

try:
    grade = float(x)
except:
    print('Bad score')
    quit()

if grade < 0.0:
    print('Bad score')
    quit()
if grade > 1.0:
    print('Bad score')
    quit()

if grade >= 0.9:
    print('A')
elif grade >= 0.8:
    print('B')
elif grade >= 0.7:
    print('C')
elif grade >= 0.6:
    print('D')
else:
    print('F')