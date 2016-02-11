#!/usr/bin/env python


# f = open("busy_day.in", "rb")
f = open("mother_of_all_warehouses.in", "rb")
rows, cols, drones_count, turns_count, max_payload = map(int, f.readline().strip().split())
# print rows, cols, drones_count, turns_count, max_payload

product_type_count, = map(int, f.readline().strip().split())
# print product_type_count

product_weights = map(int, f.readline().strip().split())

warehouse_count, = map(int, f.readline().strip().split())

warehouses = []


# print range(warehouse_count)
for w in range(warehouse_count):
  coords = map(int, f.readline().strip().split())
  product_stock = map(int, f.readline().strip().split())
  warehouses_dict = {}
  warehouses_dict["coord"] = coords
  warehouses_dict["stock"] = product_stock
  warehouses.append(warehouses_dict)

# print warehouses


order_count = int(f.readline().strip())

orders = []

for o in range(order_count):
  order_coord = map(int, f.readline().strip().split())
  order_products_count = int(f.readline().strip()) # Dummy, do not need this
  order_products = map(int, f.readline().strip().split())
  order_dict = {}
  order_dict["coord"] = order_coord
  order_dict["requests"] = order_products
  order_dict["id"] = o
  orders.append(order_dict)


my_drones = []

for d in range(drones_count):
  curr_drone = {}
  curr_drone["coord"] = warehouses[0]["coord"]
  curr_drone["busy"] = 0
  curr_drone["dest"] = None
  curr_drone["curr_w"] = 0
  curr_drone["id"] = d
  my_drones.append(curr_drone)
# print orders
