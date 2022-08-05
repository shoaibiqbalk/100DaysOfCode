# For Loop
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# List Comprehension
new_list = [n + 1 for n in numbers]

# String as List
name = "Angela"
letters_list = [letter for letter in name]

# Range as List
range_list = [n * 2 for n in range(1, 5)]

# Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
upper_case_names = [name.upper() for name in names if len(name) > 4]

# Dictionary Comprehension

import random
student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)

passed_students = {
    student: grade
    for (student, grade) in student_grades.items() if grade >= 60
}
print(passed_students)


student_dict = {
    "student": ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"],
    "score": [89, 72, 87, 82, 79, 76]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through rows of a Data Frame

for (index, row) in student_data_frame.iterrows():
    # print(row)
    print(row.student, row.score)
    if row.student == "Alex":
        print(row)