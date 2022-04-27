#!/usr/bin/env python3
def volume(length, width, height):
    """Returns the volume of a box for given dimensions"""
    return length * width * height


fmt = "Enter {:6} of the box: "
dim1 = float(input(fmt.format("length")))
dim2 = float(input(fmt.format("width")))
dim3 = float(input(fmt.format("height")))
result = volume(length=dim1, width=dim2, height=dim3)
print("The volume is:", result)

result = volume(height=dim3, length=dim1, width=dim2)
print("The volume is:", result)
