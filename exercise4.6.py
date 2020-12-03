# calculate gross pay (user input)
# find the breakdown of how much of the gross pay is regular pay and overtime pay
# 1.5x pay for overtime
# create computepay function using hours and payrate as parameters
def computepay(hours, payrate):
    if hours > 40 :
        print('overtime')
        regpay = hours * payrate
        otpay = (hours - 40) * (payrate * 0.5)
        print(regpay,otpay)
        pay = regpay + otpay
    else:
        print('regular')
        pay = hours * payrate
    return pay

x = input('enter hours: ')
y = input('enter rate of pay: ')
hours = float(x)
payrate = float(y)

pay = computepay(hours, payrate)
print('Pay:',pay)