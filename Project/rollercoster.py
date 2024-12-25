print("Welcome to rollercoster Ride")

height = int(input("Please enter your height in CM: "))
age = int(input("Please enter your Age: "))
photo = input("Do you wnat Photos  Y or N: ").lower()

bill = 0
if height > 120:
    print("You can ride")
    if age < 12:
        bill = 5
    elif age > 12 and age < 19:
        bill = 7
    elif age > 18 and age < 45:
        bill = 12
    elif age > 44 and age < 56:
        bill = 0
else:
    print("You can't ride")
if photo == "y":
    bill += 3
    print(f"The totle bill is: ${bill}")
else:
    print(f"The totle bill is: ${bill}")