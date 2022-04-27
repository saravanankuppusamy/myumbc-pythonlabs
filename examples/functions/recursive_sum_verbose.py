#!/usr/bin/env python3


def sum_to(limit, indent):
    text = "sum_to"
    print(" " * indent, text, limit)
    indent += 1
    if not limit:
        indent -= 1
        print(" " * indent, text, limit, " => ", limit)
        return limit
    result = sum_to(limit - 1, indent)
    indent -= 1
    print(" " * indent, text, limit, end="")
    print(" => {0:2} + {1:2} => {2:2}".format(limit, result, limit + result))
    return limit + result


def main():
    indent = 0
    limit = 6
    print("\nSum from 1 to", limit, "is:", sum_to(limit, indent))


main()
