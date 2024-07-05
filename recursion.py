def add_one(num):

    if (num >= 9):
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)


mynewtotal = add_one(0)
print(mynewtotal)


## Just random code below only understand

value = "y"
count = 0

while value:
    count += 1
    print(count)
    if (count == 5):
        break
    else:
        value = 0
        continue

# Here even after continue statement, the loop will check its entry condition and hence terminate