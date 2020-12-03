# calculate gross pay (user input)
# find the breakdown of how much of the gross pay is regular pay and overtime pay
# 1.5x payrate for overtime
# create error message for non-numeric input that quits the program

x = input('enter hours: ')
try:
    hours = float(x)
except:
    print('error, please enter numeric input')
    quit()

y = input('enter rate of pay: ')
try:
    payrate = float(y)
except:
    print('error, please enter numeric input')
    quit()

if hours > 40 :
    print('overtime')
    regpay = hours * payrate
    otpay = (hours - 40) * (payrate * 0.5)
    print(regpay,otpay)
    pay = regpay + otpay
else:
    print('regular')
    pay = hours * payrate
print(pay)