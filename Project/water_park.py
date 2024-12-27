# Question:
# Write a Python program that checks if a person is eligible to enter a water park. The program should:
# Ask the user to input their age.
# Determine the ticket price based on their age:
# Ages below 5: Not eligible to enter.
# Ages 5–12: Ticket price is $8.
# Ages 13–18: Ticket price is $10.
# Ages 19–60: Ticket price is $15.
# Ages 61 and above: Ticket price is $5.
# Ask the user if they want to rent a locker (additional $2).
# Calculate and display the total bill.

print("Welcome to the Run Water Park!")
age = int(input("Please enter your Age: "))

bill = 0
if age < 5:
    bill += 8
