#!/usr/bin/env python3
def the_sum(*args):
    total = 0
    print("Parameter type:", type(args), end=" ")
    for elem in args:
        total += elem
    return total


def show_results(value):
    print("Sum is: ", value)


total = the_sum(1, 2, 3, 4, 5)
show_results(total)
show_results(the_sum(5, 2, 7))
