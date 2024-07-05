greeting = "Hello, World!"
print(greeting)
line = " Python is a great language."
print(greeting + line)


# To understand python uses interpreter to execute the code, we can run the code line by line

# print("Executing line 1")  # This line will execute
# # This line will cause a NameError because variable 'x' is not defined
# print(x)
# print("Executing line 3")  # This line will not execute due to the error above


meaning = 42

if (meaning > 10):
    print("The meaning of life is greater than 10.")
else:
    print("The meaning of life is not greater than 10.")

meaning = 8

print("The meaning of life is greater than 10.") if meaning > 10 else print("The meaning of life is not greater than 10.")
# Ternary operator is a one-liner replacement for if-else statement