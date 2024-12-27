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

# Solution:
# Ask the user to input their age.
age = int(input("Enter your age: "))
# Determine the ticket price based on their age:
if age < 5:
    print("You are not eligible to enter.")
elif 5 <= age <= 12:
    ticket_price = 8
    print("Ticket price is $8.")
elif 13 <= age <= 18:
    ticket_price = 10
    print("Ticket price is $10.")
elif 19 <= age <= 60:
    ticket_price = 15
    print("Ticket price is $15.")
else:
    ticket_price = 5
    print("Ticket price is $5.")
# Ask the user if they want to rent a locker (additional $2).
locker = input("Do you want to rent a locker? (yes/no): ")
if locker == "yes":
    locker_price = 2
    print("Locker price is $2.")
else:
    locker_price = 0
    print("No locker rented.")
# Calculate and display the total bill.
total_bill = ticket_price + locker_price
print(f"Total bill: ${total_bill}")


