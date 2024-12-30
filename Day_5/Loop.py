# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

###########################

# students_scores = [90, 85, 78, 65, 88, 92, 75, 68, 72, 95, 85, 80, 90, 100, 85, 102, 115]
# max_score = 0
# for score in students_scores:
#     if score > max_score:
#         max_score = score
# print(f"The highest score is: {max_score}")

#############################################

#Range function with for loop
# FizzBuzz
# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

# e.g. it might start off like this:

# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# # ...etc

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)




# Write a program that prints all the even numbers between 1 and 50 (inclusive).
# Use the range() function and a for loop to accomplish this.
for number in range(1, 51):
    if number % 2 == 0:
        print(number)


# Sum of Multiples
# Write a program to calculate the sum of all multiples of 7 between 1 and 100 (inclusive).
# Use a for loop and the range() function.

sum = 0
for number in range(1, 101):
    if number % 7 == 0:
        sum += number
print(sum)
