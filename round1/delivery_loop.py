#!/usr/bin/env python


import sys
import math

from hake import *


def distance(a,b):
  return math.ceil( ((a["coord"][0] - b["coord"][0])**2 + (a["coord"][1] - b["coord"][1])**2)**0.5 )

# print distance([0,0], [3,4])
# print distance([0,0], [3,3])

so = sorted(orders, key=lambda x: len(x["requests"]))
# orders.sort()

print so 

#assume some calculations done here
#fuck freshmonous
while turns_count>0:
  for drone in drones:
    if drone["busy"]: continue
    chosen_warehouse=min([])
    # warehouses.closest(drone.position())
    chosen_orders=orders.getOrderFor(chosen_warehouse,drone.capacity_left)
    results+=drone.commandize(chosen_orders)
return results

# turns_count = 1
# while turns_count > 0:
#   for d_i, drone in enumerate(my_drones):
#     if not drone["busy"]:
#       curr_min_w = sys.maxint
#       target_w = None
#       target_o = None
#       for w_i, warehouse in enumerate(warehouses):
#         dw = distance(drone, warehouse)
#         wo = sys.maxint
#         for o_i, order in enumerate(orders):
#           d2 = distance(warehouse, order)
#           if d2 < wo:
#             wo = d2
#             target_o = o_i


#         if dw+wo < curr_min_w:
#           curr_min_w = d
#           target_w = w_i


#       print curr_min_w
#       # print curr_min_w

#   turns_count -= 1
