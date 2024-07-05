class JustNotCoolError(Exception):
    pass


x = 2
try:
    # raise JustNotCoolError("This just isn't cool, man.")
    # raise Exception("I'm a custom exception!")
    # print(x / 0)
    print(x / 1)
    # if type(x) is not str:
    #     raise TypeError("Only strings are allowed.")
except NameError:
    print('NameError means something is probably undefined.')
except ZeroDivisionError:
    print('Please do not divide by zero.')
except Exception as error:
    print(error)
else:
    print('No errors!')
finally:
    print("I'm going to print with or without an error.")

# finally block is always executed, regardless of whether an exception was raised or not.
# else block is executed only if no exceptions were raised.