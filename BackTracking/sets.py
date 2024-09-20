# map = set()
# neg = set()

# arr = [-50,-50,-49,-48,-48,-47,-46,-45,-45,-44,-42,-41,-41,-40,-39,-38,-38,-37,-36,-30,-29,-29,-28,-28,-27,-26,-25,-25,-25,-24,-23,-23,-23,-22,-22,-20,-20,-20,-19,-18,-18,-15,-15,-15,-15,-15,-15,-13,-12,-12,-12,-12,-9,-8,-7,-6,-6,-5,-5,-2,-1,0,1,1,2,4,8,8,10,11,11,12,14,14,14,17,18,22,22,23,23,26,26,27,27,27,28,28,28,28,29,29,29,30,30,32,32,32,32,33,34,34,35,36,36,37,37,37,38,42,42,43,44,45,45,46,46,47,48,49,49,50,50]

# for i in arr:
#     if(i < 0):
#         neg.add(i)
#     else:
#         map.add(i)

# print(neg)
# print(map)

# my_list = [-3, -2, -1, 0, 1, 2, 3]
# my_set = set()

# # Adding elements in order
# for num in my_list:
#     my_set.add(num)

# print("Original List:", my_list)
# print("Set Contents:", my_set)

from collections import OrderedDict

my_list = [-3, -2, -1, 0, 1, 2, 3]
ordered_set = OrderedDict()

for num in my_list:
    ordered_set[num] = None  # Use None as a placeholder value

print("Original List:", my_list)
print("Ordered Set Contents:", list(ordered_set.keys()))

