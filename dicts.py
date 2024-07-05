import sys 

# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Animal", guitar="Page") # constructor function

print(band)
print(band2)
print(type(band))
print(len(band))

# Access items
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# verify a key exists
print("guitar" in band)
print("triangle" in band)

# Change values (update if exists, add if not)
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"}) 

print(band)

# Remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())  # tuple
print(band)

# Delete and clear

band["drums"] = "Bonham"
print(band) 
del band["drums"]
print(band)

band2.clear()
print(band2)

# del band2
# print(band2)  # NameError

# Copy dictionaries

# band2 = band  # create a reference
# print("Bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

# sys.exit()

band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy!")
print(band)
print(band2)

# or use the dict() constructor function
band3 = dict(band)
print("Good copy!")
print(band3)


# Nested dictionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}

band2 = {
    "member1" : {
        "name": "Plant",
        "instrument": "vocals"
    },
    "member2" : {
        "name": "Page",
        "instrument": "guitar"
    }
}

# 2 ways to create nested dictionaries

print(band)
print(band2)
print(band["member1"]["name"])
print(band2["member1"]["name"])
# print(band2.member1.name) # AttributeError: 'dict' object has no attribute 'member1'

print("")
print("")
print("")
print("")



# Sets

nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicate allowed
nums = {1, 2, 2, 3}
print(nums) # {1, 2, 3}

# True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
# As 1 comes before True, 1 is kept and True is removed. Similarly, False is kept and 0 is removed. Moreover increasing order of the numbers is maintained.
print(nums) 

# check if a value is in a set
print(2 in nums)
print(7 in nums)

# but you cannot refer to an element in the set with an index position or a key

# Add a new element to a set
nums.add(8)
print(nums)

# Add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# you can use update with lists, tuples, and dictionaries, too.

# Merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# Keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)