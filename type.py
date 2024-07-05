first = 'Dave'
second = 'Gray'

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

pizza = str('Pepperoni')
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

fullname = first + ' ' + second
fullname += ' Jr.'

print(fullname)

decade = str(1920)
print('I like rock music from the ' + decade + 's.')

# Use three ''' or """ to create a multiline string
multiline = '''
Hey, how are you?                                   

I was just checking in.    
                                All good?

'''
print(multiline)


# Escape characters are used to insert special characters in strings
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s the \\coffee?'
print(sentence)

print(second)
print(second.lower())
print(second.upper())
print(second)

print(multiline)
print(multiline.title())
print(multiline.replace('good', 'great')) # this is case sensitive
print(multiline)

print('Python'.startswith('Py'))
print('Python'.endswith('on'))
print('Python'.find('th'))
print('Python3'.isalpha())
print('Python'.isalpha())
print('123'.isdigit())
print('123a'.isdigit())

print(len(multiline))
multiline += '                                '
multiline = "                          " + multiline
print(len(multiline))
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")
print('Menu'.center(20, '-'))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))
print("")

print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data types

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1)) # round to 1 decimal place

import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))  # round up
print(math.floor(gpa)) # round down

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

print(int("New York")) # this will throw an error