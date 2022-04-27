#!/usr/bin/env python3
reward_pts = {"Bryce": 500, "Heather": 2000, "Kaylie": 750,
              "Amanda": 1350, "Casey": 2400, "Jason": 800,
              "Kaylie": 25}
rule, prefix, space = "-" * 75, "\n", " "
loop = "looping through {}"
print(loop.format("dictionary"), rule, sep=prefix)
for name in reward_pts:
    print(name, reward_pts[name])

keys, values, items = ["keys()", "values()", "items()"]
print(prefix, loop.format(keys), rule, sep=prefix)
for name in reward_pts.keys():
    print(name, end=space)

print(prefix, loop.format(values), rule, sep=prefix)
for value in reward_pts.values():
    print(value, end=space)

print(prefix, loop.format(items), rule, sep=prefix)
for item in reward_pts.items():
    print(item)

fmt = "{:8}~{:>8}"
print(prefix, "Items() unpacked as keys and values", rule, sep=prefix)
print(fmt.format("Name", "Points"))
for name, points in reward_pts.items():
    print(fmt.format(name, points))

fmt = "{:>8}"
print(prefix, "Data types of returned views", rule, sep=prefix)
print(fmt.format(keys), type(reward_pts.keys()))
print(fmt.format(values), type(reward_pts.values()))
print(fmt.format(items), type(reward_pts.items()))
