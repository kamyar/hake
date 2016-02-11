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
print warehouses
def i_have_an_order(order,request,warehouse,fuck):
  warehouse=tuple(warehouse["coord"])
  order=tuple(order["coord"])
  if warehouse not in fuck:
    fuck[warehouse]={}
  if request not in fuck[warehouse]:
    fuck[warehouse][request]={}
  if order not in fuck[warehouse][request]:
    fuck[warehouse][request][order]=1
  else:
    fuck[warehouse][request][order]+=1
fuck={}
for order in so:
  sorted_warehouses = sorted(warehouses, key = lambda x : distance(x,order))
  for request in order["requests"]:
    for warehouse in sorted_warehouses:
      if warehouse["stock"][request]:
        warehouse["stock"][request]-=1
        i_have_an_order(order,request,warehouse,fuck)
        break

print fuck 

#assume some calculations done here


commands = []

# def commandize(drone, warehouse, orders):
#   pass

while turns_count>0:
  min_busy = sys.maxint
  for drone in my_drones:
    # if drone["busy"] < min_busy:
    min_busy = min(min_busy, drone["busy"])

    if not drone["busy"]:
      chosen_warehouse=min([ distance(drone, w) for w in warehouses ])
      # chosen_orders=
      # orders.getOrderFor(chosen_warehouse,drone.capacity_left)
      # results+=drone.commandize(chosen_orders)
      print chosen_warehouse

  for drone in my_drones:
    drone["busy"] -= min_busy

  raw_input()

  turns_count -= min_busy
  turns_count-=1 #  Temp


# return results

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
