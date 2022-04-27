#!/usr/bin/env python3
def volume(length, width, height):
    """Returns the volume of a box for given dimensions"""
    return length * width * height


fmt = "Enter {:6} of the box: "
dim1 = float(input(fmt.format("length")))
dim2 = float(input(fmt.format("width")))
dim3 = float(input(fmt.format("height")))
result = volume(dim1, dim2, dim3)
print("The volume is:", result)
