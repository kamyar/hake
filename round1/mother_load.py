#!/usr/bin/env python


import sys
import math

from hake import *


def distance(a,b):
  return math.ceil( ((a["coord"][0] - b["coord"][0])**2 + (a["coord"][1] - b["coord"][1])**2)**0.5 )

# print distance([0,0], [3,4])
# print distance([0,0], [3,3])

so = sorted(orders, key=lambda x: distance(x, warehouses[0]))
so = sorted(orders, key=lambda x: len(x["requests"]))
# orders.sort()

print so 


def commandize(drone_id, warehouse_id, order_id):
  delivery_dict = {}
  for r in orders[order_id]["requests"]:
    if warehouses[warehouse_id]["stock"][r] > 0:
      if my_drones[drone_id]["curr_w"] + product_weights[r] <= max_payload:
        my_drones[drone_id]["curr_w"] += product_weights[r]
        warehouses[warehouse_id]["stock"][r] -= 1
        if r in delivery_dict.keys():
          delivery_dict[r] += delivery_dict[r]
        else:
          delivery_dict[r] = 1
      else:
        break
  dist = distance(my_drones[drone_id], warehouses[warehouse_id]) + distance(warehouses[warehouse_id], orders[order_id]) + len(delivery_dict.keys())
  return False, dist, delivery_dict

paths = []
while turns_count>0: 
  min_busy = sys.maxint
  for d_i, drone in enumerate(my_drones):
    # if drone["busy"] < min_busy:

    if not drone["busy"]:
      # chosen_warehouse = 0

      target_o = so[0]
      # busy_time = commandize(d_i, 0, target_o["id"]) 
      # so = so[1:]
      # distance(drone, warehouses[0]) + distance(warehouses[0], target_o) + 1
      
      status, btime, ddic = commandize(d_i, 0, target_o)
      print status, btime
      my_drones[d_id]["busy"] = btime

      # chosen_orders=
      # orders.getOrderFor(chosen_warehouse,drone.capacity_left)
      # results+=drone.commandize(chosen_orders)
      # print chosen_warehouse
    min_busy = min(min_busy, drone["busy"])

  for drone in my_drones:
    drone["busy"] -= min_busy

  raw_input()

  turns_count -= min_busy
  turns_count-=1 #  Temp
