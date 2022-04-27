#!/usr/bin/env python3
bryce, heather, kaylie = ["Bryce", "Heather", "Kaylie"]
reward_pts = {bryce: 500, heather: 2000, kaylie: 750}
points = reward_pts.get(bryce)      # returns 500
print(bryce, points)
stephanie = "Stephanie"
points = reward_pts.get(stephanie)  # returns None
print(stephanie, points)

# Supplying a different value to return other than None
points = reward_pts.get(stephanie, 0)  # returns 0
print(stephanie, points)
print("Current Dictionary Contents:", reward_pts)
