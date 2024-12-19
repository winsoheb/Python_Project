print("Welcome to the tip calculator!")
#input from user
bill = float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give%? 10, 12, or 15? "))
split = int(input("How many pople to split the bill? "))
#calculation start
tip_p = tip / 100
total_tip = bill * tip_p
total_bill = bill + total_tip
pay = total_bill / split
#output start
print(f"Each person should pay: ${pay}")
pay_1 = (round(pay, 2)) #rount of method
print(f"Each person should pay: ${pay_1}")
