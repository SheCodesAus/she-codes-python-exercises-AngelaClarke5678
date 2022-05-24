from ast import Return
from collections import defaultdict
from typing import final

prices = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
}

quantity = {
    "Baby Spinach": 1,
    "Hot Chocolate": 3,
    "Crackers": 2,
    "Bacon": 1,
    "Carrots": 4,
    "Oranges": 2
}

# quantity = {
#     "Baby Spinach": 2,
#     "Hot Chocolate": 1,
#     "Crackers": 4,
#     "Bacon": 0,
#     "Carrots": 8,
#     "Oranges": 5
# }

# final_list = defaultdict(list) #https://stackoverflow.com/questions/5946236/how-to-merge-multiple-dicts-with-same-key-or-different-key
# for item in (prices, quantity):
#     for key, value in item.items():
#         final_list[key].append(value)
# print(final_list)

# final_list = {}
# for item in prices:
#   shopping_list = f"{quantity[item]} {item} {prices[item]}"
#   final_list.items(shopping_list)
# #  price_groceries =  [sum(prices[item] * quantity[item] for item in prices)]
# print(final_list)

# for item in final_list:
#     output = f"{quantity[item] }* {quantity[item]}"
# print(output)

for item, price in quantity.items():
    final_price = quantity[item] * prices[item]
    print(f"{quantity[item]} {item} @ ${prices[item]} = ${final_price}")
