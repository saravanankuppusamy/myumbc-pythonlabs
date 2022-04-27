#!/usr/bin/env python3
grades = ("A", "B", "C", "D", "F")
points = ("90-100", "80-89", "70-79", "60-69", "00-59")
delimeter = "\t"
fmt = "{} : {}"

for grade in grades:
    print(grade, end=delimeter)
print()

for a_tuple in enumerate(grades):
    print(fmt.format(a_tuple[0], a_tuple[1]), end=delimeter)
print()

# Unpacking the tuple from enumerate
for i, grade in enumerate(grades, start=1):
    print(fmt.format(i, grade), end=delimeter)
print()

# Process the two tuples in parallel
for index, grade in enumerate(grades):
    print(fmt.format(grade, points[index]))
