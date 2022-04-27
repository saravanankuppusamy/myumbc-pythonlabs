#!/usr/bin/env python3
newline = "\n"
newlines = newline * 2
names = """Smith Johnson Williams Brown Jones Lee Garcia Rodriguez White
           Martinez Anderson Thomas Hernandez Moore Lopez Davis"""
names = names.split()
print("Original:", names, sep=newline, end=newlines)
# Sort by name (Alphabetically)
print("Alphabetically:", sorted(names), sep=newline, end=newlines)
# Sort by length
print("By Length:", sorted(names, key=len), sep=newline)
