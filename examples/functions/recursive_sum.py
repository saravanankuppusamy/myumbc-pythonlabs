#!/usr/bin/env python3
def sum_to(limit):
    if not limit:     # This is the termination condition
        return limit

    return limit + sum_to(limit-1)  # This is where the recursion is


def main():
    limit = 6
    print("Sum from 1 to", limit, "is:", sum_to(limit))


main()
