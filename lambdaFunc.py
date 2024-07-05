from functools import reduce

squared = lambda num : num * num
add_two = lambda num : num + 2
sum_total = lambda num1,num2 : num1 + num2

# sum_total = lambda (num1,num2) : num1 + num2 
# this is not the correct way to pass multiple arguments to a lambda function, we cannot use brackets

print(squared(5))
print(add_two(5))
print(sum_total(5,6))

def funcBuilder(x) :
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(5))
print(addTwenty(5))

numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))


###############################

odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))

numbers = [1, 2, 3, 4, 5]

#################################

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

print(sum(numbers, 10))


names = ['Dave Gray', 'Sara Ito', 'John Jacob Jingleheimerschmidt']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)