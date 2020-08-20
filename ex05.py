'''
Write a script in python to find min, max and average marks of a class consists of 10 students
'''

marks = [76, 81, 45, 70, 67, 80, 92, 65, 55, 69]

# Average
sum_total = 0
for mark in marks:
    sum_total += mark

average = sum_total / len(marks)
print(f"Average marks of a class is {average}")

# Minimum and maximimun Marks
min_marks, max_marks = marks[0], marks[0]
for mark in marks:
    if mark < min_marks:
        min_marks = mark
    if mark > max_marks:
        max_marks = mark

print(f"Minimum marks in the class is {min_marks}")
print(f"Maximum marks in the class is {max_marks}")
