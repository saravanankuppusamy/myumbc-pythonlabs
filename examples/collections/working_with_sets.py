#!/usr/bin/env python3
# Define the strings that are used multiple times
prompts = ["Please enter some first names ", "again ",
           "to delete "]
end = "\n" * 2  # define value to use as end in prints
delimeter = ""  # define delimeter to use to join prompts together

msg1 = prompts[0]                      # Using str.join to join together
msg2 = delimeter.join(prompts[:2])     # strings by avoiding explicit string
msg3 = delimeter.join(prompts)         # concatentation

name_list = input(msg1).split()
unique_names = set(name_list)
backedup_names = set(unique_names)
print(unique_names, end=end)

# Check to see if name exists prior to adding
name_list = input(msg2).split()
for name in name_list:
    if name not in unique_names:
        unique_names.add(name)
    else:
        print("\t", name, "already exists and is ignored")
print(unique_names, end=end)

# Update contents of set with contents of a list
name_list = input(msg2).split()
unique_names.update(name_list)
print(unique_names, end=end)

# Check to see if name exists prior to removing
name_list = input(msg3).split()
for name in name_list:
    if name in unique_names:
        unique_names.remove(name)

# Discard words without checking first
name_list = input(msg3).split()
for name in name_list:
    unique_names.discard(name)
print(unique_names, end=end)

# Check the relationship of one set to another
print()
print("Original:", backedup_names)
print("Current :", unique_names, "\n")
print("Original is subset of Current ? ",
      backedup_names.issubset(unique_names))
print("Current is superset of Original ? ",
      unique_names.issuperset(backedup_names))

# Pop each element from the set until it is empty
print("Popping each name from set: ", unique_names)
while unique_names:
    print(unique_names.pop(), end=" ")
print()
