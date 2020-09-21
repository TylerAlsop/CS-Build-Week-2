
# def merge_packages(items, limit):
#     print(f'items: {items}')
#     print(f'limit: {limit}')

#     for item_i in items:
#         for item_j in items[item_i + 1 :]:
#             if item_i + item_j == limit:
#                 two_items = [item_i, item_j]
#                 two_items.sort()
#                 print(two_items)
#                 return two_items
#     return []



# merge_packages([4, 6, 10, 15, 16], 21)


items_1 = [4, 6, 10, 15, 16]

for item_i in items_1:
    for item_j in items_1[items_1[item_i]:]:
        print(item_j)