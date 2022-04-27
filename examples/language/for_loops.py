#!/usr/bin/env python3
word = "Hello"
print(word)
for each_character in word:
    print(each_character, end="\t")

indent = "\n\t"
space = " "
fmt = "\nrange({}):"
print(fmt.format(5), end=indent)
for i in range(5):
    print(i, end=space)

print(fmt.format("5, 10"), end=indent)
for i in range(5, 10):
    print(i, end=space)

print(fmt.format("-5, 9, 3"), end=indent)
for i in range(-5, 9, 3):
    print(i, end=space)

print()
