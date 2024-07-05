name = "Dave"
count = 1

def another():
    color = "blue"
    global count
    count = 2
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Dave")
    print(color)

another()
print(count)

# comment global and nonlocal and see what happens, first comment one at a time then both to understand the difference