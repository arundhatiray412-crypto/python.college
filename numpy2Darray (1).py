# 2D array of marks
marks = [
    [80, 70, 90],
    [60, 75, 85],    #2d array in a list
    [90, 88, 95],
    [55, 65, 70],
    [78, 82, 80]
]

#  Max
print("Maximum marks:", max(max(row) for row in marks))

#  Min
print("Minimum marks:", min(min(row) for row in marks))

#  Avg
total = sum(sum(row) for row in marks)
average = total / 15

print("Average marks:", average)

# Max subject-wise
print("Maximum marks subject-wise:")

for j in range(3):
    maximum = max(marks[i][j] for i in range(5))
    print("Subject", j + 1, ":", maximum)

# Average  subject-wise
print("Average marks subject-wise:")

for j in range(3):
    total = sum(marks[i][j] for i in range(5))
    average = total / 5
    print("Subject", j + 1, ":", average)
   

# Add 10 marks if Subject 1 marks are less than 50
for student in marks:
    if student[0] < 50:
        student[0] = student[0] + 10

# Updated Subject 1 marks
print("\nSubject 1 marks after adding 10:")
for i in range(5):
    print("Student", i + 1, ":", marks[i][0])