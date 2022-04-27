#!/usr/bin/env python3
numbers = [3, 1, -10, 54, 75, 29]
words = ["Hello", "Goodbye", "goodbye", "hello"]
label1, label2 = ("  Unsorted:", "  Sorted:")
print("Basic sorting of a list.")
print(label1, numbers, words)
numbers.sort()
words.sort()
print(label2, numbers, words, "\n")

numbers.append(33)  # add to numbers so it is no longer in any particular order
words.append("hi")  # add to words so it is no longer in any particular order
print("Basic sorting of a list in reverse.")
print(label1, numbers, words)
numbers.sort(reverse=True)
words.sort(reverse=True)
print(label2, numbers, words, "\n")
