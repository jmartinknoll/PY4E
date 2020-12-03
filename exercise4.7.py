# prompt for score between 0.0 and 1.0
# error message for score that is out of range
# print a letter grade using the following table:
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# use computegrade as a function to return a grade as a string

def computegrade(grade):
    if grade < 0.0 or grade > 1.0:
        return('Score out of range')
    if grade >= 0.9:
        return('A')
    elif grade >= 0.8:
        return('B')
    elif grade >= 0.7:
        return('C')
    elif grade >= 0.6:
        return('D')
    else:
        return('F')

x = input('Enter score (0.0 - 1.0):')
try:
    grade = float(x)
except:
    print('Bad score')
    quit()

print(computegrade(grade))