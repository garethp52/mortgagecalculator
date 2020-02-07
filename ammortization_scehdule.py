# print ("Enter the loan amount required:")
# principal = float(input())
#
# print ("Enter the interest rate as a decimal:")
# interestRateYear = float(input())
#
# print ("Enter the loan term, in years:")
# periodYears = int(input())
#
# periodMonths = periodYears * 12
# interestRateMonth =  interestRateYear/12
# x = interestRateMonth * (1 + interestRateMonth) ** periodMonths
# y = (1 + interestRateMonth) ** periodMonths - 1
# amortizationAmount = (x / y) * principal
#
#
# number = 0
# startingBalance = principal
# endingBalance = principal

# while number <= periodMonths:
#     interest = startingBalance * interestRateMonth
#     principalPayment = amortizationAmount - interest
#     number += 1
#     endingBalance = startingBalance - principalPayment
#     print(number, round(startingBalance, 2), round(interest, 2), round(principalPayment, 2), round(endingBalance, 2))
#     startingBalance = endingBalance
#
#

def ammortization(principle, interestRateYear, periodYears):
    periodMonths = periodYears * 12
    interestRateMonth = interestRateYear / 12
    x = interestRateMonth * (1 + interestRateMonth) ** periodMonths
    y = (1 + interestRateMonth) ** periodMonths - 1
    amortizationAmount = (x / y) * principle

    number = 0
    startingBalance = principle
    endingBalance = principle

    while number <= periodMonths:
        interest = startingBalance * interestRateMonth
        principlePayment = amortizationAmount - interest
        number += 1
        endingBalance = startingBalance - principlePayment
        print (number, round(startingBalance, 2), round(interest, 2), round(principlePayment, 2),
              round(endingBalance, 2))
        return [(number, round(startingBalance, 2), round(interest, 2), round(principlePayment, 2),
            round(endingBalance, 2))]
        # a = ((number, round(startingBalance, 2), round(interest, 2), round(principlePayment, 2),
        #      round(endingBalance, 2)))
        # print (a)



        startingBalance = endingBalance

ammortization(50000, 0.075, 5)

# def test(principle, interestRateYear, periodYears):
#     return (principle + interestRateYear + periodYears)