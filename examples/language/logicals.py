#!/usr/bin/env python3
zero = 0
x = y = zero
if x == zero and y == zero:
    print("x and y are", zero)

if x == zero or y == zero:
    print("x or y or both are", zero)

low = 10
high = 20
the_same_response = "x not between {} and {}".format(low, high)
if not (x >= low and x <= high):
    print(the_same_response)

if (x < low or x > high):
    print(the_same_response)
