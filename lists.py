import sys

users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptylist = []

print("Dave" in users)
print("Dave" in data)
print("Dave" in emptylist)

print(users[0])
print(users[-2])
# print(users[-4]) # IndexError: list index out of range
# print(emptylist[0]) # IndexError: list index out of range

print(users.index('Sara'))

print(users[0:2])
# print(users[1:0]) # empty list is returned
# print(users[2:0]) # empty list is returned
print(users[1:])
print(users[-3:-1])
# print(users[-1:-1]) # empty list is returned
# print(users[-1:-3]) # empty list is returned

print(len(data))

users.append('Elsa')
print(users)

users += ['Jason']
# users += 'Jason' # this will add each character of the string as an element in the list
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Bob')
print(users)

users[2:2] = ['Eddie', 'Alex'] # this will insert elements at index 2
print(users)

users[1:3] = ['Robert', 'JPJ'] # this will replace the elements at index 1 and 2
print(users)

users[1:3] = [] # another way to remove
print(users)

users.remove('Bob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data # this will delete the entire list so the next print line will cause an error
data.clear() # this will remove all elements from the list but the list will still exist
print(data)

users.sort()
print(users)
users[1:2] = ['dave'] # this will replace the element at index 1
users.sort(key = str.lower) # case insensitive sort
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse() # reverse the list
print(nums)

# nums.sort(reverse=True) # sort in descending order, the original list is modified
# print(nums)

print(sorted(nums, reverse=True)) # returns a new list, the original list is not modified
print(nums)

numscopy = nums.copy() 
mynums = list(nums)
mycopy = nums[:]
# 3 ways to copy a list

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums) # original list is not modified, only the copy is sorted

print(type(nums)) # <class 'list'>

mylist = list([1, "Neil", True]) # list() constructor
print(mylist) 



# Tuples



mytuple = tuple(('Dave', 42, True))
anothertuple = (1, 4, 2, 8, 2, 2)
# Read-only list, cannot be modified

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

# (one, *two, hey) = anothertuple
(one, two, *hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))