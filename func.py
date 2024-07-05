def hello_world():
    print("Hello world!")

hello_world()

# for i in range(5):
#     print("Hello")

# for i in range(5):
#     for j in range(i+1):
#         print("*")
#     print("")

# def isPrime(num):
#     if(type(num) is not int):
#         return
    
#     if num < 2:
#         return False
#     for i in range(2,num):
#         if(num%i == 0):
#             return False
#     return True

# check = isPrime('y')
# check = isPrime(6)
# check = isPrime(7)
# print(check)

# def sum(num1=0, num2=0):
#     if (type(num1) is not int or type(num2) is not int):
#         return 0
#     return num1 + num2

# total = sum(7, '')
# total = sum(7, 2)
# print(total)


def multiple_items(*args):
    print(args)
    print(type(args))

    for item in args:
        print(item)

multiple_items("Dave", "John", "Sara")

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

    print(kwargs.keys())
    print(kwargs.values())
    print(kwargs.items())

    for key,value in kwargs.items():
        print(key + " : " + value)

    for item in kwargs:
        print(item + " : " + kwargs[item])

mult_named_items(first="Dave", last="Gray")




# Just for practice and understanding 

# diction = {
#     1 : 11,
#     2 : 22,
#     3 : 33
# }

# print(diction[1])