"""
File: paymentPlanner.py
Author: Clint Kline
Last Modified: 5/30/2021
Purpose: To Estimate a payment schedule for loans and financed purchases.
"""
# input collection
price = (float(input("\nPurchase Price: ")))
# example "12" for one year, "120" for 10 years
months = (float(input("Loan Duration(in months): ")))
downPayment = (float(input("Down Payment: ")))
interestRate = (float(input("Interest Rate(as a decimal): "))
                )  # example: .045 = 4.5%

# other variables
subTotal = price - downPayment
total = subTotal + (subTotal * interestRate)
payment = total / months

# comfirm input
print("\nprice:   $%0.2f" % price)
print("months:   $%0.2f" % months)
print("downPayment:   $%0.2f" % downPayment)
print("interestRate:   $%0.2f" % interestRate)
print("subTotal:   $%0.2f" % subTotal)
print("total w/int after down payment:   $%0.2f" % total)
print("payment:   $%0.2f" % payment, "\n")

# print table headers
print("%-10s%-18s%-15s%-15s%-15s%-15s" % ("Month #:", "Init. Balance:",
      "Interest:", "Principal:", "Payment:", "Rem. Balance"))

# begin list build
if months > 0:
    duration = []
    month = 0

    # add values to list "duration" equal to number of months entered
    while months != 0:
        month += 1
        duration.append(month)
        months -= 1

# handle no input in months variable
else:
    print("Please enter a Duration.")


# begin table build
remDur = len(duration)
while total > 0 and remDur > 0:
    # loop through each month in list "duration" to create a table of payments equal to the amount of months entered by user
    for i in duration:
        balance = total
        interest = balance * interestRate / remDur
        remDur -= 1
        remBal = balance - (payment + interest)
        principal = payment - interest
        # display table row
        print("%-10s$%-17.2f$%-14.2f$%-14.2f$%-14.2f$%-14.2f" %
              (i, balance, interest, principal, payment, remBal))
        total = remBal

# end
