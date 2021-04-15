# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python

def dirReduc(arr):
  opposite = {"NORTH" : "SOUTH", "SOUTH" : "NORTH", "EAST" : "WEST", "WEST" : "EAST"}
  new_plan = []
  for d in arr:
    if new_plan and new_plan[-1] == opposite[d]:
      new_plan.pop()
    else:
      new_plan.append(d)
    print(new_plan)
  return new_plan


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
# print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))