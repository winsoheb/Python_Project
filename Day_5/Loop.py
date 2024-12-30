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

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)




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



# Even Numbers Printer
# Write a program that prints all the even numbers between 1 and 50 (inclusive).
# Use the range() function and a for loop to accomplish this.


# Sum of Multiples
# Write a program to calculate the sum of all multiples of 7 between 1 and 100 (inclusive).
# Use a for loop and the range() function.


# Custom FizzBuzz
# Modify the FizzBuzz program to work with a custom range:
# Accept two inputs from the user: a starting number and an ending number.
# Implement the same rules of FizzBuzz for numbers in that range.


# Reverse Counting
# Write a program that prints all numbers from 100 to 1 in descending order using the range() function.


# Prime Checker
# Write a program that prints all prime numbers between 1 and 50.
# Hint: Use nested loops to check divisibility of each number.

# Multiplication Table
# Write a program that prints the multiplication table of a given number (1 to 10).
# Accept the number as user input.


# Factorial Calculation
# Write a program to calculate the factorial of a number using a for loop.
# Accept the number as user input.


# Leap Year Finder
# Write a program to find all the leap years between 2000 and 2100.
# Hint: A year is a leap year if it is divisible by 4 but not by 100, unless it is also divisible by 400.


# Sum of Digits
# Write a program that calculates the sum of the digits of each number from 1 to 20.
# For example:
# For 12, the sum is 1+2=3.
# For 19, the sum is 1+9=10.


# Custom Divisibility Check
# Write a program where the user inputs two numbers, x and y, and a range 𝑛(e.g., 1 to 100).
# Print "X" if a number in the range is divisible by  𝑥
# Print "Y" if a number in the range is divisible by 𝑦
# Print "XY" if a number in the range is divisible by both 𝑥 and 𝑦
# Otherwise, print the number.

