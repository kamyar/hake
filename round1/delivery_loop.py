#!/usr/bin/env python


import sys
import math

from hake import *


def distance(a,b):
  return math.ceil( ((a["coord"][0] - b["coord"][0])**2 + (a["coord"][1] - b["coord"][1])**2)**0.5 )

# #print distance([0,0], [3,4])
# #print distance([0,0], [3,3])

so = sorted(orders, key=lambda x: len(x["requests"]))
# orders.sort()

#print so 
#print warehouses
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

#print fuck 
suck = fuck

#assume some calculations done here


commands = []

# def commandize(drone, warehouse, orders):
#   pass

# def capacity_left(d_id):
#   return max_payload - my_drones[d_id]["curr_w"]



coord_to_order = {}
for o in orders:
  coord = tuple(o["coord"])
  coord_to_order[coord] = o["id"]

all_commands=[]
while turns_count > 0:
  min_busy = sys.maxint
  for drone in my_drones:
    # if drone["busy"] < min_busy:

    if not drone["busy"]:
      dist_warehouse,chosen_warehouse=min([ (distance(drone, w),w) for w in warehouses ])
      t = tuple(chosen_warehouse["coord"])
      items = suck[t]
      commands=[]
      capacity_left = max_payload
      for it in items:
        for dit in items[it]:
          if 0<items[it][dit]<=capacity_left:
            commands+=[[chosen_warehouse["id"],it,dit,items[it][dit]]]
            capacity_left-=items[it][dit]
            items[it][dit]=0
          elif 0<items[it][dit]<=capacity_left:
            commands+=[[chosen_warehouse["id"], it, dit, capacity_left]]
            items[it][dit]-=capacity_left
            capacity_left=0
          if capacity_left==0: break
        if capacity_left==0:break
      # chosen_orders=commands
      # orders.getOrderFor(chosen_warehouse,drone.capacity_left)
      # results+=drone.commandize(chosen_orders)
      # #print chosen_warehouse
      dist=math.ceil(dist_warehouse)
      prev=chosen_warehouse["coord"]
      for x in commands:
        dist+=distance({"coord":prev},{"coord":x[2]})
        prev=x[2]
      commands=[drone["id"]]+commands
      drone["busy"]=dist
      #print dist
    min_busy = min(min_busy, drone["busy"])

  for drone in my_drones:
    drone["busy"] -= min_busy
  all_commands+=[commands]
  #print min_busy
  if min_busy==sys.maxint or min_busy==0: turns_count=0
  #raw_input()
  if turns_count>0: turns_count -= min_busy
  #print turns_count
  #turns_count-=1 #  Temp
# #print all_commands


for command in all_commands:
  for c in command[1:]:
    d_id = command[0]
    c[2] = coord_to_order[tuple(c[2])]
    print d_id, "L", c[0], c[1], c[3]
  for c in command[1:]:
    d_id = command[0]
    # c[2] = coord_to_order[tuple(c[2])]
    print d_id, "D", c[2], c[1], c[3]  

  # print command
  # break
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


      # #print curr_min_w
      #print curr_min_w

#   turns_count -= 1
