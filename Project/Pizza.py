print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L: ")
pepperoni = input("Do you wnat pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you wnat extra cheese? Y or N: ")

# s = 15
# m = 20
# l = 25
#
# if size == "s":
#     if pepperoni == "y":
#         bill = s + 2
#     if extra_cheese == "y":
#         bill= s+3
#     print(f"Your final bill is: {bill}")
# elif size == "m":
#     print(f"Your final bill is: {m}")
# elif size == "l":
#     print(f"Your final bill is: {l}")
#
# else:
#     print(f"Your final bill is: ")

#todo: work out how much they need to pay based on their size choice
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You type the wrong inputs.")
#todo: work out how much to add to their bill based on their pepperoni choice.
if pepperoni == "Y":
    if size == "S":
        bill +=2
    else:
        bill += 3

#todo: work out their final amount based on whether if they want extra cheese.
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: {bill}.")