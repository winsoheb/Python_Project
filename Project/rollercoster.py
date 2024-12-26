# print("Welcome to rollercoster Ride")
#
# height = int(input("Please enter your height in CM: "))
# age = int(input("Please enter your Age: "))
# photo = input("Do you want Photos  Y or N: ").lower()
#
# bill = 0
# if height > 120:
#     print("You can ride")
#     if age < 12:
#         bill = 5
#     elif age > 12 and age < 19:
#         bill = 7
#     elif age > 18 and age < 45:
#         bill = 12
#     elif age > 44 and age < 56:
#         bill = 0
# else:
#     print("You can't ride")
# if photo == "y":
#     bill += 3
#     print(f"The total bill is: ${bill}")
# else:
#     print(f"The total bill is: ${bill}")
##################################  New    ###################################################

print("Welcome to rollercoster Ride")
height = int(input("Please enter your height in CM: "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
            print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12")
    photo = input("Do you want Photos  Y or N: ").lower()
    if photo != "y":
        pass
    else:
        bill += 3
        print(f"The total bill is: ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")