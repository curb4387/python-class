# Write your program here
DOWN_PAYMENT_PERCENT = 0.10
ANNUAL_INTEREST_PERCENT = 0.12
MONTHLY_PAYMENT_PERCENT = 0.05

purchase_price = float(input("Enter the purchase price: "))
down_payment = purchase_price * DOWN_PAYMENT_PERCENT
monthly_interest_rate = ANNUAL_INTEREST_PERCENT / 12
monthly_payment = purchase_price * MONTHLY_PAYMENT_PERCENT
starting_balance = purchase_price - down_payment
monthly_interest_owed = starting_balance * monthly_interest_rate
principal_pay = monthly_payment - monthly_interest_owed
ending_balance = starting_balance - monthly_payment
month = 1

print("Month", "%17s" % "Starting Balance", "%16s" % "Interest to Pay", "%17s" % "Principal to Pay", "%8s" % "Payment", "%15s" % "Ending Balance")

while ending_balance > 0:
    ending_balance = starting_balance - monthly_payment
    print("%2d" % month, "%14.2f" % starting_balance, "%14.2f" % round(monthly_interest_owed, 2), "%16.2f" % principal_pay, "%16.2f" % monthly_payment, "%16.2f" % ending_balance)
    month += 1
    starting_balance = ending_balance
    monthly_interest_owed = starting_balance * monthly_interest_rate
    principal_pay = monthly_payment - monthly_interest_owed