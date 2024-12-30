# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

###########################

students_scores = [90, 85, 78, 65, 88, 92, 75, 68, 72, 95, 85, 80, 90, 100, 85, 102, 115]
max_score = 0
for score in students_scores:
    if score > max_score:
        max_score = score
print(f"The highest score is: {max_score}")